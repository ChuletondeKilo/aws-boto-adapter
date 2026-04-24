from .dtos import *

import boto3
    
class SSMService:
    def __init__(self, session: boto3.Session):
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