from pydantic import BaseModel

####### Get Secret Values ######

class GetSecretValueParams(BaseModel):
    """SSM GetSecretValue Params Class"""
    Name: str
    WithDecryption: bool = False
