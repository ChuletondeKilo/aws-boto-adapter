from pydantic import Field, BaseModel
from typing import Union, Literal

import boto3

####### Get Secret Values ######

class GetSecretValueParams(BaseModel):
    """SSM GetSecretValue Params Class"""
    Name: str
    WithDecryption: bool = False
