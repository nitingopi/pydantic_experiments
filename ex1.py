from datetime import datetime
from typing import Tuple
from uuid import uuid4

from pydantic import BaseModel, Field


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]


m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
# print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
# print(m.dimensions)
#> (10, 20)

class User(BaseModel):
    id: Field()
    name: str = 'Jane Doe'

user = User(id=123,name='Naveen')
print(user.model_fields_set)
# print(user.model_dump())
# assert user.id == 123 
# assert isinstance(user.name, str)

# user.model_validate({'id': 1, 'name': 'String'})
