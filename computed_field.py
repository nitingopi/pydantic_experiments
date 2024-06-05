from pydantic import BaseModel, computed_field

class Box(BaseModel):
    width: float
    height: float
    depth: float

    @computed_field
    def volume(self) -> float:
        return self.width * self.height * self.depth
    

box = Box(width=3, height=4,depth=5)
print(box.model_dump())    