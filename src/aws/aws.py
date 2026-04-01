import logging
from typing import Any

from .dtos import ClientTypeDispatcher, operations
import common

from botocore.config import Config
import boto3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = Config(
   region_name = 'eu-west-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 3,
        'mode': 'standard'
    }
)

@common.handler_decorator
def execute_method(aws_client, operation_dto: operations) -> Any:

    method = getattr(aws_client, operation_dto.method_name)

    return method(**operation_dto.method_params.model_dump())


@common.handler_decorator
def instantiate_client(client_type: str, api_level: str, config: Config) -> Any:

    session = boto3.session.Session()

    logger.info(f"Instantiating boto3 client with config {config}.")

    match api_level:

        case "client":
    
            api_client = session.client(client_type, config=config)
        
        case "resource":

            api_client = session.resource(client_type, config=config)
    
        case _:

            logger.error("Missing information regarding api level.")
            
            raise Exception("Missing information regarding api level.")

    return api_client

@common.handler_decorator
def validate_data(client_type: str, method_name: str, method_params: dict) -> ClientTypeDispatcher:

    input = {
            "client_type": client_type,
            "method_dispatcher": {
                "operation": {
                    "method_name": method_name,
                    "method_params": method_params
                }
            }
        }

    return ClientTypeDispatcher(client=input) # ty: ignore[invalid-argument-type]

def execute(client_type: str, method_name: str, method_params: dict) -> dict:

    """Executes the operation with the correct AWS client"""

    logger.info("Validating AWS Call Data.")

    aws_client_dto = validate_data(client_type, method_name, method_params)
    
    logger.info("Instantiating boto3 session.")

    aws_client = instantiate_client(aws_client_dto.client.client_type, aws_client_dto.client.method_dispatcher.operation.api_level, config)

    logger.info("Executing AWS Call")
    
    response = execute_method(aws_client, aws_client_dto.client.method_dispatcher.operation)

    return response
