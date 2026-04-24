from pydantic import Field, BaseModel

# ===== SSM Method Classes (one per method) =====

####### Get Parameter ######

class GetParameterParams(BaseModel):
    """SSM GetParameters Params Class"""
    Name: str
    WithDecryption: bool = False

####### Get Parameters ######

class GetParametersParams(BaseModel):
    """SSM GetParameters Params Class"""
    Names: list[str]
    WithDecryption: bool = False