from pydantic import Field, BaseModel
from typing import Union, Literal, Optional

# ===== SecretsManager Method Classes (one per method) =====

####### Get Secret ######

class SecretsManagerGetSecretParams(BaseModel):
    """SSM GetParameters Params Class"""
    SecretId: str
    VersionId: Optional[str] = None
    VersionStage: Optional[str] = None

class SecretsManagerGetSecretValue(BaseModel):
    """DTO for SecretsManager GetSecretValue operation"""
    method_name: Literal["get_secret_value"] = Field(default="get_secret_value")
    method_params: SecretsManagerGetSecretParams

# ===== Dispatcher Union =====
SecretsManagerOperation = Union[
    SecretsManagerGetSecretValue,
]

# ===== Dispatcher Class =====
class SecretsManagerDispatcher(BaseModel):
    """Routes to correct SecretsManager operation based on discriminator"""
    operation: SecretsManagerOperation = Field(discriminator="method_name")

# ===== Client Class =====
class SecretsManagerClient(BaseModel):
    
    client_type: Literal['secretsmanager']
    method_dispatcher: SecretsManagerDispatcher