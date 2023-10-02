import datetime
import json
from typing import List, Optional
from fastapi import APIRouter, HTTPException
from app.server.data.bikes import filter_bikes_by_time, process_bike_helper

from app.server.schemas import bike_schema
from app.server.redis import redis_client

router = APIRouter(
    prefix="/bikes",
    tags=["bikes"],
)

BIKE_INDEX_API = "https://bikeindex.org:443/api/v3"

@router.get("/", response_model=List[bike_schema.Bike])
async def get_stolen_bikes(
        number_of_days_since_stolen: Optional[int] = None,
        number_of_months_since_stolen: Optional[int] = None,
        stolen_datetime_min: Optional[datetime.datetime] = None,
        stolen_datetime_max: Optional[datetime.datetime] = None,
        location: str = "IP",
        manufacturer: Optional[str] = None,
        distance: int = 10,
        page: int = 1,
        include_images: bool = False,
        ):
    """A function to get stolen bikes from the bike index api, and filter them by time stolen.
       Returning all possible results would be reckless, so we will limit the results to 100 per page
       and use the page parameter to get the next page of results.

       The API docs are here: https://bikeindex.org/documentation/api_v3#!/search/GET_version_search_format_get_0

       Distance is in miles, and the default is 10 miles. The default location is the IP address of the user."""

    # validate the inputs
    conditions = [
        number_of_days_since_stolen is not None,
        number_of_months_since_stolen is not None,
        stolen_datetime_min is not None or stolen_datetime_max is not None,
    ]
    if sum(conditions) > 1:
        raise HTTPException(status_code=400, detail="Exactly one argument must be non-null.")

    # reduce number of API calls by caching the results
    # note we are caching the location, which is user specified
    # for a production app, there are a large number of ways to write one location
    # for example, "New York" and "New York, NY" are the same place, but would be cached separately
    # so we'd want to constrain the user input to a specific format (dropdown in UI for a system like Pulse could be good)
    # or we could use google maps API to get a formatted address, if it made technical sense
    # I exclude the keys that have a large number of possible values
    # because this would cause a lot of cache misses and not be very useful
    # also, I exclude the base64 images since that will be a lot of extra data but it might make sense to cache them
    # reduce request time from 5.56s to 5ms !
    redis_key = f"bikes:{location}:{distance}:{page}"
    if not any([stolen_datetime_min, stolen_datetime_max, include_images, manufacturer]):
        cached_bikes = redis_client.get(redis_key)
        if cached_bikes:
            cached_json = json.loads(cached_bikes)
            return [bike_schema.Bike(**json.loads(bike)) for bike in cached_json]

    manufacturer_filter = f"&manufacturer={manufacturer}" if manufacturer else ""
    url = f"{BIKE_INDEX_API}/search?page={page}&per_page=10&location={location}&distance={distance}&stolenness=stolen{manufacturer_filter}"
    
    # make the request for the bikes
    bikes_to_return = await process_bike_helper(url, include_images)
    
    # filter by stolen time, which checks if filter is requested and sets the min and max values
    bikes_to_return = await filter_bikes_by_time(bikes_to_return, number_of_days_since_stolen, number_of_months_since_stolen, stolen_datetime_min, stolen_datetime_max)

    # set redis cache to revalidate every 24 hours
    if not any([stolen_datetime_min, stolen_datetime_max, include_images, manufacturer]):
        redis_client.set(redis_key, json.dumps([bike.json() for bike in bikes_to_return]), ex=60*60*24)

    return bikes_to_return


