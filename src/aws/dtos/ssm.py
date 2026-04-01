from pydantic import Field, BaseModel
from typing import Union, Literal

# ===== SSM Method Classes (one per method) =====

####### Get Parameter ######

class SSMGetParameterParams(BaseModel):
    """SSM GetParameters Params Class"""
    Name: str
    WithDecryption: bool = False

class SSMGetParameter(BaseModel):
    """DTO for SSM GetParameter operation"""
    method_name: Literal["get_parameter"] = Field(default="get_parameter")
    api_level: Literal["resource"] = Field(default="resource")
    method_params: SSMGetParameterParams

####### Get Parameters ######

class SSMGetParametersParams(BaseModel):
    """SSM GetParameters Params Class"""
    Names: list[str]
    WithDecryption: bool = False

class SSMGetParameters(BaseModel):
    """DTO for SSM GetParameters operation"""
    method_name: Literal["get_parameters"] = Field(default="get_parameters")
    api_level: Literal["resource"] = Field(default="resource")
    method_params: SSMGetParametersParams

# ===== Dispatcher Union =====
SSMOperation = Union[
    SSMGetParameter,
    SSMGetParameters
]

# ===== Dispatcher Class =====
class SSMOperationDispatcher(BaseModel):
    """Routes to correct SSM operation based on discriminator"""
    operation: SSMOperation = Field(discriminator="method_name")

# ===== Client Class =====
class SSMClient(BaseModel):
    
    client_type: Literal['ssm']
    method_dispatcher: SSMOperationDispatcher
