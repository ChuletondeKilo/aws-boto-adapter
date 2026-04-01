from .secretsmanager import SecretsManagerClient, SecretsManagerOperation
from .ssm import SSMClient, SSMOperation
from .s3 import S3Client, S3Operation

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

operations = Union[S3Operation, SSMOperation, SecretsManagerOperation]

# ===== Dispatcher Class =====
class ClientTypeDispatcher(BaseModel):

    client: clients = Field(discriminator="client_type")

__all__ = ['ClientTypeDispatcher', 'operations', 'clients']