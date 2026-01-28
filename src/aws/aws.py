import logging

from .dtos import ClientTypeDispatcher

from botocore.config import Config
import boto3

logger = logging.getLogger(__name__)

config = Config(
   region_name = 'eu-west-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 3,
        'mode': 'standard'
    }
)

def execute(client_obj: ClientTypeDispatcher) -> dict:

    """Executes the operation with the correct AWS client"""
    
    session = boto3.session.Session()

    aws_client = session.client(client_obj.client.client_type, config=config)
    
    method = getattr(aws_client, client_obj.client.method_dispatcher.operation.method_name)

    response = method(**client_obj.client.method_dispatcher.operation.method_params.model_dump())

    return response


def aws_services(client_type: str, method_name: str, method_params: dict) -> dict:

    # Validate input params via dataclass instantiation and execute operation

    input = {
            "client_type": client_type,
            "method_dispatcher": {
                "operation": {
                    "method_name": method_name,
                    "method_params": method_params
                }
            }
        }

    aws_client = ClientTypeDispatcher(client=input) # ty: ignore[invalid-argument-type]
    
    response = execute(aws_client)

    return response