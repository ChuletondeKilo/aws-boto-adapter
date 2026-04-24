from typing import Union

from .ssm import *
from .s3 import *
from .param_store import *

service_classes = Union[SSMService, S3Service, ParamStoreService]