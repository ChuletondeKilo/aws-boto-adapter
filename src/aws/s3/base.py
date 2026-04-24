from .dtos import *

import boto3
    
class S3Service:
    def __init__(self, session: boto3.Session):
        self._client = session.client('s3')
        self._resource = session.resource('s3')

    def get_object(self, params: S3PutObjectParams):
        """
        Obtiene un objeto de S3.
        Auto-valida los campos usando Pydantic.
        """
        # Convertimos el modelo de Pydantic a un dict que Boto3 entienda
        payload = params.model_dump(by_alias=True, exclude_none=True)
        return self._client.get_object(**payload)