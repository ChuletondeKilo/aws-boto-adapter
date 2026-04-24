from pydantic import Field, BaseModel
from typing import Union, Literal
import boto3

from .dtos import *

class SSMService:
    def __init__(self, session: boto3.Session):
        self._client = session.client('ssm')

    def get_parameter(self, params: GetSecretParams):
        """
        Obtiene un parámetro de SSM. 
        Auto-valida los campos usando Pydantic.
        """
        # Convertimos el modelo de Pydantic a un dict que Boto3 entienda
        payload = params.model_dump(by_alias=True, exclude_none=True)
        return self._client.get_parameter(**payload)

class S3Service:
    def __init__(self, session: boto3.Session):
        self._client = session.client('ssm')

    def get_parameter(self, params: GetSecretParams):
        """
        Obtiene un parámetro de SSM. 
        Auto-valida los campos usando Pydantic.
        """
        # Convertimos el modelo de Pydantic a un dict que Boto3 entienda
        payload = params.model_dump(by_alias=True, exclude_none=True)
        return self._client.get_parameter(**payload)

class ParamStoreService:
    def __init__(self, session: boto3.Session):
        self._client = session.client('ssm')

    def get_parameter(self, params: GetSecretParams):
        """
        Obtiene un parámetro de SSM. 
        Auto-valida los campos usando Pydantic.
        """
        # Convertimos el modelo de Pydantic a un dict que Boto3 entienda
        payload = params.model_dump(by_alias=True, exclude_none=True)
        return self._client.get_parameter(**payload)

class AWSServiceDescriptor:
    """Descriptor que gestiona la creación perezosa de servicios."""
    def __init__(self, service_class: SSMService, service_name: str):
        self.service_class: SSMService = service_class
        self.service_name: str = service_name
        self.attr_name: str = f"_{service_name}_instance"

    # Este descriptor nos asegura que solo iremos creando instancias de los servicios que se llamen.
    # Si un servicio aun no se ha llamado con "MyAWS.ssm", el atributo ssm de MyAWS solo contendra la clase
    def __get__(self, instance, owner) -> SSMService:
        # Nos cubre de si el usuario llama a la clase sin haberla instanciado MyAWS.s3, por ejemplo
        if instance is None:
            # Devolvemos el descriptor pero en modo instancia, lo que incluye la información del init
            return self
        
        # Si el servicio no existe en la instancia de MyAWS, lo creamos
        # Aqui nos cubrimos de que no se haya instanciado
        if not hasattr(instance, self.attr_name):
            print(f"DEBUG: Inicializando {self.service_name}...")
            # Usamos la sesión que vive en MyAWS
            service_obj = self.service_class(instance.session)
            setattr(instance, self.attr_name, service_obj)
            
        return getattr(instance, self.attr_name)

class MyAWS:
    def __init__(self, profile=None, region=None):
        self.session = boto3.Session(profile_name=profile, region_name=region)

    # Definimos los servicios usando el descriptor
    # ¡Cero lógica repetida aquí!
    # Queremos que el __get__ nos devuelva una instancia de SSMService para ofrecer los metodos
    ssm = AWSServiceDescriptor(SSMService, "ssm") # <-- Queda inicializada la clase SSMService
    s3 = AWSServiceDescriptor(S3Service, "s3")
    secrets = AWSServiceDescriptor(ParamStoreService, "secretsmanager")