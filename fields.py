from pydantic import BaseModel, Field, UUID5
from uuid import uuid5

class Foo(BaseModel):
    positive: int = Field(gt=0)
    non_negative: int = Field(ge=0)
    negative: int = Field(lt=0)
    non_positive: int = Field(le=0)
    even: int = Field(multiple_of=2)
    # id:str = Field(pattern='^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
    id:UUID5
    love_for_pydantic: float = Field(allow_inf_nan=True)


foo = Foo(
    positive=1,
    non_negative=1,
    negative=-1,
    non_positive=0,
    even=2,
    id='5144a659-0fcb-488e-95c2-c898788d34fr',
    love_for_pydantic=float('inf'),
)
# print(foo)

