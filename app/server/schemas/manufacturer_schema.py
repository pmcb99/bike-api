import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl

class ManufacturerBase(BaseModel):
    name: str
    company_url: str # found an empty string in the response so cant use HttpUrl
    id: int
    frame_maker: Optional[bool] # found it returned a null value in the response
    image: Optional[str]
    description: Optional[str]
    short_name: str
    slug: str

class Manufacturer(ManufacturerBase):
    id: int

    class Config:
        from_attributes = True
