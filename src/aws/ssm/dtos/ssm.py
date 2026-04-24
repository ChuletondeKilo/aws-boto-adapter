from pydantic import Field, BaseModel
from typing import Union, Literal

# ===== SSM Method Classes (one per method) =====

####### Get Parameter ######

class GetParameterParams(BaseModel):
    """SSM GetParameters Params Class"""
    Name: str
    WithDecryption: bool = False

class GetParameter(BaseModel):
    """DTO for SSM GetParameter operation"""
    method_name: Literal["get_parameter"] = Field(default="get_parameter")
    api_level: Literal["resource"] = Field(default="resource")
    method_params: GetParameterParams
