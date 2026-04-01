from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field

class BlackCat(BaseModel):
    pet_type: Literal['cat']
    color: Literal['black']
    black_name: str

class WhiteCat(BaseModel):
    pet_type: Literal['cat']
    color: Literal['white']
    white_name: str

Cat = Annotated[Union[BlackCat, WhiteCat], Field(discriminator='color')]

# Let's inspect what Cat is
print("=" * 60)
print("1. What is Cat?")
print("=" * 60)
print(f"type(Cat) = {type(Cat)}")
print(f"Cat = {Cat}")
print()

# Try to instantiate Cat directly
print("=" * 60)
print("2. Can we instantiate Cat directly?")
print("=" * 60)
try:
    instance = Cat()
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
print()

# What about BlackCat?
print("=" * 60)
print("3. Can we instantiate BlackCat?")
print("=" * 60)
instance = BlackCat(pet_type='cat', color='black', black_name='Midnight')
print(f"✓ Success: {instance}")
print()

# What metadata is stored in Cat?
print("=" * 60)
print("4. What metadata is in Cat?")
print("=" * 60)
print(f"Cat.__metadata__ = {Cat.__metadata__}")
print(f"Type of metadata: {type(Cat.__metadata__[0])}")
print(f"Metadata content: {Cat.__metadata__[0]}")
print()

# What's the underlying type?
print("=" * 60)
print("5. What's the underlying type?")
print("=" * 60)
print(f"Cat.__origin__ = {Cat.__origin__}")
print(f"Cat.__args__ = {Cat.__args__}")
