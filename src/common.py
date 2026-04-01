from typing import Callable, ParamSpec, TypeVar
from functools import wraps
import logging

P = ParamSpec("P")
R = TypeVar("R")

logger = logging.getLogger(__name__)

def handler_decorator(func: Callable[P, R]) -> Callable[P, R]:

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:

        logger.info(f"Executing function: {func.__name__} with args: \n {args} \n and kwargs: \n {kwargs}") # ty: ignore[unresolved-attribute]

        try:

            result = func(*args, **kwargs)
        
        except Exception as e:

            logger.error(f"Caught an Error on function {func.__name__} with message: \n {e}") # ty: ignore[unresolved-attribute]
            
            raise Exception(f"Caught an Error on function {func.__name__} with message: \n {e}") # ty: ignore[unresolved-attribute]

        else:

            logger.info(f"Function {func.__name__} executed succesfully.") # ty: ignore[unresolved-attribute]

        return result
    
    return wrapper
