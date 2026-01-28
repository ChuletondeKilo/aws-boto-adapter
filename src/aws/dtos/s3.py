from pydantic import Field, BaseModel
from typing import Union, Literal, Optional

# ===== S3 Method Classes (one per method) =====

####### Get Object ######

class S3GetObjectParams(BaseModel):
    """S3 GetObject Params Class"""
    Bucket: str
    Key: str
    VersionId: Optional[str] = None
    SSECustomerAlgorithm: Optional[str] = None

class S3GetObject(BaseModel):
    """DTO for S3 GetObject operation"""
    method_name: Literal["get_object"] = Field(default="get_object")
    method_params: S3GetObjectParams

####### Put Object ######

class S3PutObjectParams(BaseModel):
    """S3 PutObject Params Class"""
    Bucket: str
    Key: str
    Body: bytes
    ContentType: Optional[str] = None
    ServerSideEncryption: Optional[str] = None

class S3PutObject(BaseModel):
    """DTO for S3 PutObject operation"""
    method_name: Literal["put_object"] = Field(default="put_object")
    method_params: S3PutObjectParams

# ===== Dispatcher Union =====
S3Operation = Union[
    S3GetObject,
    S3PutObject,
]

# ===== Dispatcher Class =====
class S3Dispatcher(BaseModel):
    """Routes to correct S3 operation based on discriminator"""
    operation: S3Operation = Field(discriminator="method_name")

# ===== Client Class =====
class S3Client(BaseModel):
    
    client_type: Literal['s3']
    method_dispatcher: S3Dispatcher