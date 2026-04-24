"""AWS Boto Adapter - Lazy-loading AWS service wrapper with strong typing."""

from .main import MyAWS
from .aws import SSMService, S3Service, ParamStoreService

__version__ = "0.1.0"

__all__ = [
    "MyAWS",
    "SSMService",
    "S3Service",
    "ParamStoreService",
]
