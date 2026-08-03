from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=500)
    price: float = Field(gt=0)


class ProductResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    owner_id: int

    model_config = {
        "from_attributes": True
    }