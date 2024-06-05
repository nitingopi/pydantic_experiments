import json
from enum import Enum

from typing import Annotated

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class FooBar(BaseModel):
    count: int
    size: float | None = None

class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    not_given = 'not_given'

class MainModel(BaseModel):
    model_config =  ConfigDict(title='Main')
    foo_bar: FooBar
    gender: Annotated[Gender | None, Field(alias='Gender')] = None
    snap: int = Field(
        42,
        title='The Snap',
        description='This is the value of snap',
        gt=30,
        lt=50,
    ) 

main_model_schema = MainModel.model_json_schema()
print(json.dumps(main_model_schema, indent=2))           