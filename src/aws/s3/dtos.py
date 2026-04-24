from pydantic import Field, BaseModel
from typing import Optional, Literal

####### Put Object ######

class S3PutObjectParams(BaseModel):
    """S3 PutObject Params Class"""
    Bucket: str
    Key: str
    Body: bytes
    ContentType: Optional[str] = None
    ServerSideEncryption: Optional[str] = None
