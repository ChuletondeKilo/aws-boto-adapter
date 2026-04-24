from pydantic import Field, BaseModel
from typing import Union, Literal

import boto3

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

####### Get Parameters ######

class GetParametersParams(BaseModel):
    """SSM GetParameters Params Class"""
    Names: list[str]
    WithDecryption: bool = False

class GetParameters(BaseModel):
    """DTO for SSM GetParameters operation"""
    method_name: Literal["get_parameters"] = Field(default="get_parameters")
    api_level: Literal["resource"] = Field(default="resource")
    method_params: GetParametersParams

# ===== Dispatcher Union =====
SSMOperation = Union[
    GetParameter,
    GetParameters
]

# ===== Dispatcher Class =====
class SSMOperationDispatcher(BaseModel):
    """Routes to correct SSM operation based on discriminator"""
    operation: SSMOperation = Field(discriminator="method_name")

# ===== Client Class =====
class SSMClient(BaseModel):
    
    client_type: Literal['ssm']
    method_dispatcher: SSMOperationDispatcher