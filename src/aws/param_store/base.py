from .dtos import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    
    import boto3
    
class ParamStoreService:
    def __init__(self, session: boto3.Session):
        self._client = session.client('ssm')
        self._resource = session.resource('ssm')

    def get_parameter(self, params: GetParameterParams):
        """
        Obtiene un parámetro de SSM. 
        Auto-valida los campos usando Pydantic.
        """
        # Convertimos el modelo de Pydantic a un dict que Boto3 entienda
        payload = params.model_dump(by_alias=True, exclude_none=True)
        return self._client.get_parameter(**payload)