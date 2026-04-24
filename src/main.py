from __future__ import annotations

from typing import Self, TypeVar, Generic, overload

from aws import *

import boto3

T = TypeVar('T', SSMService, S3Service, ParamStoreService)

# Fer AWSServiceDescriptor(Generic[T]) ens permet despres assignar atributs amb AWSServiceDescriptor[SSMService] i ell sap que tot lo que
# hi ha dins de la classe es amb T = SSMService.
class AWSServiceDescriptor(Generic[T]):
    """Descriptor que gestiona la creación perezosa de servicios."""
    def __init__(self: Self, service_class: type[T], service_name: str) -> None:
        self.service_class: type[T] = service_class
        self.service_name: str = service_name
        self.attr_name: str = f"_{service_name}_instance"

    # Este descriptor nos asegura que solo iremos creando instancias de los servicios que se llamen.
    # Si un servicio aun no se ha llamado con "MyAWS.ssm", el atributo ssm de MyAWS solo contendra la clase
    @overload
    def __get__(self: Self, instance: None, owner: type) -> "AWSServiceDescriptor[T]": ...
    @overload
    def __get__(self: Self, instance: "MyAWS", owner: type) -> T: ...
    def __get__(self: Self, instance: "MyAWS | None", owner: type) -> "AWSServiceDescriptor[T] | T":
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
    session: boto3.Session
    
    def __init__(self, profile: str | None = None, region: str | None = None) -> None:
        self.session = boto3.Session(profile_name=profile, region_name=region)

    # Definimos los servicios usando el descriptor
    # ¡Cero lógica repetida aquí!
    # Queremos que el __get__ nos devuelva una instancia de SSMService para ofrecer los metodos
    ssm: AWSServiceDescriptor[SSMService] = AWSServiceDescriptor(SSMService, "ssm")  # <-- Queda inicializada la clase SSMService
    s3: AWSServiceDescriptor[S3Service] = AWSServiceDescriptor(S3Service, "s3")
    secrets: AWSServiceDescriptor[ParamStoreService] = AWSServiceDescriptor(ParamStoreService, "secretsmanager")