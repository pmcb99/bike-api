import logging

from fastapi import FastAPI

from app.server.models import models
from fastapi import FastAPI

from app.server.routers import bikes

logger = logging.getLogger(
    __name__
)  # the __name__ resolve to "main" since we are at the root of the project.
# This will get the root logger since no logger in the configuration has this name.

app = FastAPI()

app.include_router(bikes.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}