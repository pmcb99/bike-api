import datetime
from typing import List, Optional
from pydantic import BaseModel, HttpUrl

from app.server.schemas.manufacturer_schema import ManufacturerBase

class BikeBase(BaseModel):
    title: Optional[str]
    date_stolen: Optional[int]
    date_stolen_readable: Optional[datetime.datetime]
    description: Optional[str]
    frame_model: Optional[str]
    is_stock_img: Optional[bool]
    large_img: Optional[str]
    location_found: Optional[str]
    manufacturer_name: Optional[str]
    external_id: Optional[str]
    registry_name: Optional[str]
    registry_url: Optional[str]
    serial: Optional[str]
    status: Optional[str]
    stolen: Optional[bool]
    stolen_coordinates: Optional[List[float]]
    stolen_location: Optional[str]
    thumb: Optional[str]
    image_base64: Optional[str]
    pdf_base64: Optional[str]=None
    url: Optional[HttpUrl]
    year: Optional[int]
    frame_colors: Optional[List[str]]
    manufacturer_information: Optional[ManufacturerBase]

class Bike(BikeBase):
    id: int

    class Config:
        from_attributes = True
