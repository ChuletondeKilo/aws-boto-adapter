from .secretsmanager import SecretsManagerClient
from .ssm import SSMClient
from .s3 import S3Client

from pydantic import BaseModel, Field
from typing import Union
from botocore.config import Config

config = Config(
   region_name = 'eu-west-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 3,
        'mode': 'standard'
    }
)

# ===== Dispatcher Union =====
clients = Union[SSMClient, SecretsManagerClient, S3Client]

# ===== Dispatcher Class =====
class ClientTypeDispatcher(BaseModel):

    client: clients = Field(discriminator="client_type")

__all__ = ['ClientTypeDispatcher']