import base64
import datetime
from typing import List, Optional
from fastapi import APIRouter
from httpx import request
from app.server.schemas import bike_schema
from app.server.schemas.manufacturer_schema import ManufacturerBase
from app.utils.pdf_base64 import encode_image_to_pdf_base64


router = APIRouter(
    prefix="/bikes",
    tags=["bikes"],
)

BIKE_INDEX_API = "https://bikeindex.org:443/api/v3"

async def fetch_url(url: str)->Optional[str]:
    try:
        response = request(method='GET', url=url)
    except Exception as e:
        raise e
    return response

async def fetch_manufacturer_information(manufacturer_name: str) -> Optional[ManufacturerBase]:
    """Fetch manufacturer info from API endpoint"""
    url = f"{BIKE_INDEX_API}/manufacturers/{manufacturer_name}"
    response = await fetch_url(url)
    if res_data := response.json():
        return ManufacturerBase(**res_data.get("manufacturer")) if res_data.get("manufacturer") else None
    return None

async def encode_image(image_url: str) -> Optional[str]:
    response = await fetch_url(image_url)
    return base64.b64encode(response.content) if response.content else None

async def process_bike_data(bikes: List[dict], include_images: bool) -> List[bike_schema.Bike]:
    bikes_to_return = []
    for bike in bikes:
        readable_stolen_date = datetime.datetime.fromtimestamp(bike['date_stolen']) if bike['date_stolen'] else None
        manufacturer_information = await fetch_manufacturer_information(bike.get('manufacturer_name'))

        # encode the image to base64 if it exists and is requested
        if bike.get('thumb') and include_images:
            image_base64 = await encode_image(bike['thumb'])
            base_64_pdf = encode_image_to_pdf_base64(image_url=bike["thumb"], filename=f"bike_{bike['id']}.pdf", save_pdf_file=False)

        else:
            image_base64 = None
            base_64_pdf = None

        # encode the image to pdf if it exists and is requested
        bikes_to_return.append(bike_schema.Bike(
            manufacturer_information=manufacturer_information,
            image_base64=image_base64,
            date_stolen_readable=readable_stolen_date,
            pdf_base64=base_64_pdf,
            **bike
        ))
    return bikes_to_return

async def filter_bikes_by_time(bikes_to_return: List[bike_schema.Bike], number_of_days_since_stolen: Optional[int], number_of_months_since_stolen: Optional[int], stolen_datetime_min: Optional[datetime.datetime], stolen_datetime_max: Optional[datetime.datetime]):
    if number_of_days_since_stolen is not None:
        stolen_datetime_min = datetime.datetime.now() - datetime.timedelta(days=number_of_days_since_stolen)
    elif number_of_months_since_stolen is not None:
        stolen_datetime_min = datetime.datetime.now() - datetime.timedelta(days=30*number_of_months_since_stolen)

    # these will be set if days/months requested
    if stolen_datetime_min is not None:
        bikes_to_return = [bike for bike in bikes_to_return if (bike.date_stolen and datetime.datetime.fromtimestamp(float(bike.date_stolen)).replace(tzinfo=None) >= stolen_datetime_min.replace(tzinfo=None))]
    if stolen_datetime_max is not None:
        bikes_to_return = [bike for bike in bikes_to_return if (bike.date_stolen and datetime.datetime.fromtimestamp(float(bike.date_stolen)).replace(tzinfo=None) <= stolen_datetime_max.replace(tzinfo=None))]
    return bikes_to_return

async def fetch_bikes(url: str, include_images: bool):
    response = await fetch_url(url)
    bikes = response.json().get('bikes', [])
    return bikes

async def process_bike_helper(url, include_images: bool):
    # single responsibility principle - this function should only process the bikes
    bikes = await fetch_bikes(url, include_images)
    return await process_bike_data(bikes, include_images)