from .dtos import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    
    import boto3
    
class SecretsService:
    def __init__(self, session: boto3.Session) -> None:
        self._client = session.client('ssm')
        self._resource = session.resource('ssm')

    def get_secret(self, params: GetSecretValueParams):
        """
        Obtiene un secreto de SSM. 
        Auto-valida los campos usando Pydantic.
        """
        # Convertimos el modelo de Pydantic a un dict que Boto3 entienda
        payload = params.model_dump(exclude_none=True)
        return self._client.get_secret(**payload)