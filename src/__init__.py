"""AWS Boto Adapter - Lazy-loading AWS service wrapper with strong typing."""

from .main import AWSInterface
from .aws import SecretsService, S3Service, ParamStoreService

__version__ = "0.1.0"

__all__ = [
    "AWSInterface",
    "SecretsService",
    "S3Service",
    "ParamStoreService",
]
