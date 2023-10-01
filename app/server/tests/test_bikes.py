import pytest
from unittest.mock import patch, AsyncMock
from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.server.app import app  # Adjust the import path according to your project structure
from app.server.routers import bikes
from app.server.schemas.bike_schema import Bike  # Adjust the import path according to your project structure

client = TestClient(app)

    # Replace this with the actual dict list you want to use for testing
mock_bikes_list = [
  {
    "title": "2023 Nishiki 8040337",
    "date_stolen": 1696174912,
    "date_stolen_readable": "2023-10-01T16:41:52",
    "description": "Nishiki Pueblo 24\" girls mountain bike",
    "frame_model": "8040337",
    "is_stock_img": False,
    "large_img": "https://files.bikeindex.org/uploads/Pu/753729/large_01111_R4m1Uhovhn_0CI0t2_1200x900.jpg",
    "location_found": None,
    "manufacturer_name": "Nishiki",
    "external_id": None,
    "registry_name": None,
    "registry_url": None,
    "serial": "8040337",
    "status": "stolen",
    "stolen": True,
    "stolen_coordinates": None,
    "stolen_location": "US",
    "thumb": "https://files.bikeindex.org/uploads/Pu/753729/small_01111_R4m1Uhovhn_0CI0t2_1200x900.jpg",
    "image_base64": None,
    "pdf_base64": None,
    "url": "https://bikeindex.org/bikes/1673797",
    "year": 2023,
    "frame_colors": [
      "Green"
    ],
    "manufacturer_information": {
      "name": "Nishiki",
      "company_url": "",
      "id": 243,
      "frame_maker": True,
      "image": "",
      "description": "",
      "short_name": "Nishiki",
      "slug": "nishiki"
    },
    "id": 1673797
  },
  {
    "title": "2014 Hero Splendor",
    "date_stolen": 1696171065,
    "date_stolen_readable": "2023-10-01T15:37:45",
    "description": None,
    "frame_model": "Splendor",
    "is_stock_img": False,
    "large_img": None,
    "location_found": None,
    "manufacturer_name": "Hero",
    "external_id": None,
    "registry_name": None,
    "registry_url": None,
    "serial": "4920",
    "status": "stolen",
    "stolen": True,
    "stolen_coordinates": [
      28.76,
      77.2
    ],
    "stolen_location": "Delhi, 110084, IN",
    "thumb": None,
    "image_base64": None,
    "pdf_base64": None,
    "url": "https://bikeindex.org/bikes/1673777",
    "year": 2014,
    "frame_colors": [
      "Black"
    ],
    "manufacturer_information": None,
    "id": 1673777
  },
  {
    "title": "2013 Giant TCX 2",
    "date_stolen": 1696168800,
    "date_stolen_readable": "2023-10-01T15:00:00",
    "description": "ALUXX SL-Grade Aluminum w/ Eyelets",
    "frame_model": "TCX 2",
    "is_stock_img": False,
    "large_img": "https://files.bikeindex.org/uploads/Pu/753714/large_IMG_1604.jpeg",
    "location_found": None,
    "manufacturer_name": "Giant",
    "external_id": None,
    "registry_name": None,
    "registry_url": None,
    "serial": "Unknown",
    "status": "stolen",
    "stolen": True,
    "stolen_coordinates": [
      51.07,
      -114.06
    ],
    "stolen_location": "Calgary, T2E 3B7, CA",
    "thumb": "https://files.bikeindex.org/uploads/Pu/753714/small_IMG_1604.jpeg",
    "image_base64": None,
    "pdf_base64": None,
    "url": "https://bikeindex.org/bikes/1673768",
    "year": 2013,
    "frame_colors": [
      "Black",
      "Red",
      "White"
    ],
    "manufacturer_information": {
      "name": "Giant (and LIV)",
      "company_url": "http://www.giant-bicycles.com/",
      "id": 153,
      "frame_maker": True,
      "image": "",
      "description": "",
      "short_name": "Giant",
      "slug": "giant"
    },
    "id": 1673768
  },
  {
    "title": "Trek unicycle",
    "date_stolen": 1696165545,
    "date_stolen_readable": "2023-10-01T14:05:45",
    "description": None,
    "frame_model": None,
    "is_stock_img": False,
    "large_img": "https://files.bikeindex.org/uploads/Pu/753700/large_IMG_7802.png",
    "location_found": None,
    "manufacturer_name": "Trek",
    "external_id": None,
    "registry_name": None,
    "registry_url": None,
    "serial": "wtu131c3022k",
    "status": "stolen",
    "stolen": True,
    "stolen_coordinates": [
      42.88,
      -78.74
    ],
    "stolen_location": "Cheektowaga, NY 14227, US",
    "thumb": "https://files.bikeindex.org/uploads/Pu/753700/small_IMG_7802.png",
    "image_base64": None,
    "pdf_base64": None,
    "url": "https://bikeindex.org/bikes/1673737",
    "year": None,
    "frame_colors": [
      "Blue"
    ],
    "manufacturer_information": {
      "name": "Trek",
      "company_url": "http://www.trekbikes.com/us/en/",
      "id": 47,
      "frame_maker": True,
      "image": "",
      "description": "",
      "short_name": "Trek",
      "slug": "trek"
    },
    "id": 1673737
  },
  {
    "title": "2022 Radio Flyer",
    "date_stolen": 1696165200,
    "date_stolen_readable": "2023-10-01T14:00:00",
    "description": None,
    "frame_model": None,
    "is_stock_img": False,
    "large_img": None,
    "location_found": None,
    "manufacturer_name": "Radio Flyer",
    "external_id": None,
    "registry_name": None,
    "registry_url": None,
    "serial": "dont have atm",
    "status": "stolen",
    "stolen": True,
    "stolen_coordinates": [
      33.97,
      -118.42
    ],
    "stolen_location": "Playa Vista, CA 90094, US",
    "thumb": None,
    "image_base64": None,
    "pdf_base64": None,
    "url": "https://bikeindex.org/bikes/1673739",
    "year": 2022,
    "frame_colors": [
      "Brown"
    ],
    "manufacturer_information": {
      "name": "Radio Flyer",
      "company_url": "http://www.radioflyer.com/trikes.html",
      "id": 276,
      "frame_maker": True,
      "image": "",
      "description": "",
      "short_name": "Radio Flyer",
      "slug": "radio_flyer"
    },
    "id": 1673739
  },
  {
    "title": "2004 Trek 5500",
    "date_stolen": 1696153154,
    "date_stolen_readable": "2023-10-01T10:39:14",
    "description": "OCLV 120 Carbon, no pedals",
    "frame_model": "5500",
    "is_stock_img": False,
    "large_img": "https://files.bikeindex.org/uploads/Pu/753696/large_Vintage-Road-Bikes-gear-patrol-Trek-2004.jpg",
    "location_found": None,
    "manufacturer_name": "Trek",
    "external_id": None,
    "registry_name": None,
    "registry_url": None,
    "serial": "Unknown",
    "status": "stolen",
    "stolen": True,
    "stolen_coordinates": None,
    "stolen_location": "US",
    "thumb": "https://files.bikeindex.org/uploads/Pu/753696/small_Vintage-Road-Bikes-gear-patrol-Trek-2004.jpg",
    "image_base64": None,
    "pdf_base64": None,
    "url": "https://bikeindex.org/bikes/1673691",
    "year": 2004,
    "frame_colors": [
      "Yellow or Gold",
      "Blue",
      "Red"
    ],
    "manufacturer_information": {
      "name": "Trek",
      "company_url": "http://www.trekbikes.com/us/en/",
      "id": 47,
      "frame_maker": True,
      "image": "",
      "description": "",
      "short_name": "Trek",
      "slug": "trek"
    },
    "id": 1673691
  },
  {
    "title": "Felt Dispatch 9/80",
    "date_stolen": 1696147623,
    "date_stolen_readable": "2023-10-01T09:07:03",
    "description": "",
    "frame_model": "Dispatch 9/80",
    "is_stock_img": False,
    "large_img": "https://files.bikeindex.org/uploads/Pu/752927/large_IMG_20230927_190752_HDR.jpg",
    "location_found": None,
    "manufacturer_name": "Felt",
    "external_id": None,
    "registry_name": None,
    "registry_url": None,
    "serial": "IS04210DSP80AJ90404651",
    "status": "stolen",
    "stolen": True,
    "stolen_coordinates": None,
    "stolen_location": "US",
    "thumb": "https://files.bikeindex.org/uploads/Pu/752927/small_IMG_20230927_190752_HDR.jpg",
    "image_base64": None,
    "pdf_base64": None,
    "url": "https://bikeindex.org/bikes/1672202",
    "year": None,
    "frame_colors": [
      "Black",
      "Yellow or Gold"
    ],
    "manufacturer_information": {
      "name": "Felt",
      "company_url": "http://www.feltbicycles.com/",
      "id": 136,
      "frame_maker": True,
      "image": "",
      "description": "",
      "short_name": "Felt",
      "slug": "felt"
    },
    "id": 1672202
  },
  {
    "title": "Hover-1 Journey e-scooter",
    "date_stolen": 1696140000,
    "date_stolen_readable": "2023-10-01T07:00:00",
    "description": None,
    "frame_model": "Journey",
    "is_stock_img": False,
    "large_img": "https://files.bikeindex.org/uploads/Pu/753658/large_IMG_2170.jpeg",
    "location_found": None,
    "manufacturer_name": "Hover-1",
    "external_id": None,
    "registry_name": None,
    "registry_url": None,
    "serial": "Unknown",
    "status": "stolen",
    "stolen": True,
    "stolen_coordinates": [
      32.88,
      -117.24
    ],
    "stolen_location": "La Jolla, CA 92092, US",
    "thumb": "https://files.bikeindex.org/uploads/Pu/753658/small_IMG_2170.jpeg",
    "image_base64": None,
    "pdf_base64": None,
    "url": "https://bikeindex.org/bikes/1673628",
    "year": None,
    "frame_colors": [
      "Blue",
      "Purple",
      "Stickers tape or other cover-up"
    ],
    "manufacturer_information": None,
    "id": 1673628
  },
  {
    "title": "2023 Specialized rock jumper",
    "date_stolen": 1696122000,
    "date_stolen_readable": "2023-10-01T02:00:00",
    "description": None,
    "frame_model": "rock jumper",
    "is_stock_img": False,
    "large_img": "https://files.bikeindex.org/uploads/Pu/753605/large_IMG_3355.jpeg",
    "location_found": None,
    "manufacturer_name": "Specialized",
    "external_id": None,
    "registry_name": None,
    "registry_url": None,
    "serial": "Wsbc026042047t",
    "status": "stolen",
    "stolen": True,
    "stolen_coordinates": [
      34.1,
      -118.06
    ],
    "stolen_location": "Temple City, CA 91780, US",
    "thumb": "https://files.bikeindex.org/uploads/Pu/753605/small_IMG_3355.jpeg",
    "image_base64": None,
    "pdf_base64": None,
    "url": "https://bikeindex.org/bikes/1673497",
    "year": 2023,
    "frame_colors": [
      "Black"
    ],
    "manufacturer_information": {
      "name": "Specialized",
      "company_url": "http://www.specialized.com/us/en/home/",
      "id": 307,
      "frame_maker": True,
      "image": "",
      "description": "",
      "short_name": "Specialized",
      "slug": "specialized"
    },
    "id": 1673497
  }
]

mock_bikes_list_models = [Bike(**bike) for bike in mock_bikes_list]

@pytest.mark.asyncio
async def test_get_stolen_bikes():

    with patch('app.server.routers.bikes.process_bike_helper', new_callable=AsyncMock, return_value=mock_bikes_list) as fetch_bikes_mock, \
         patch('app.server.routers.bikes.filter_bikes_by_time', new_callable=AsyncMock, side_effect=lambda bikes, *args, **kwargs: bikes) as filter_bikes_mock:

        response = client.get(
            "/bikes",
        )

    assert response.status_code == 200, response.text
    assert response.json() == mock_bikes_list

    # Ensuring the mocked methods are called once
    fetch_bikes_mock.assert_called_once()
    filter_bikes_mock.assert_called_once()



@pytest.mark.asyncio
async def test_get_stolen_bikes_too_many_time_filters():
    with patch('app.server.routers.bikes.process_bike_helper', new_callable=AsyncMock) as fetch_bikes_mock:
        
        response = client.get(
            "/bikes",
            params={"number_of_days_since_stolen": 7, "number_of_months_since_stolen": 1}  # Multiple filtering params should raise HTTPException
        )

    assert response.status_code == 400, response.text


@pytest.mark.asyncio
async def test_get_stolen_bikes_filter_time_trivial():
    with patch('app.server.routers.bikes.process_bike_helper', new_callable=AsyncMock, return_value=mock_bikes_list_models) as fetch_bikes_mock:
        response = client.get(
            "/bikes",
            params={"number_of_days_since_stolen": 0}  
        )

    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.asyncio
async def test_get_stolen_bikes_filter_time_nontrivial():
    with patch('app.server.routers.bikes.process_bike_helper', new_callable=AsyncMock, return_value=mock_bikes_list_models) as fetch_bikes_mock:
        response = client.get(
            "/bikes",
            params={"number_of_days_since_stolen": 100}  
        )

        assert response.status_code == 200
        assert response.json() != []


@pytest.mark.asyncio
async def test_get_stolen_bikes_images():
    # have to remove some fields to avoid pydantic errors when passing in two values for a single field
    mock_bike_list_with_no_readable_date = [
        bike for bike in mock_bikes_list
    ]
    for i in range(len(mock_bike_list_with_no_readable_date)):
        mock_bike_list_with_no_readable_date[i].pop("date_stolen_readable")
        mock_bike_list_with_no_readable_date[i].pop("image_base64")
        mock_bike_list_with_no_readable_date[i].pop("pdf_base64")
        mock_bike_list_with_no_readable_date[i].pop("manufacturer_information")

    with patch('app.server.data.bikes.fetch_bikes', new_callable=AsyncMock, return_value=mock_bike_list_with_no_readable_date) as fetch_bikes_mock:
        response = client.get(
            "/bikes",
            params={"include_images": True} 
        )

    assert response.status_code == 200
    assert response.json()[0]
    