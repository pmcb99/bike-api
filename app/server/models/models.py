
from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Bike(Base):
    __tablename__ = 'bikes'
    
    id = Column(Integer, primary_key=True, index=True)
    date_stolen = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    frame_colors = Column(JSON, nullable=True)  
    frame_model = Column(String, nullable=True)
    is_stock_img = Column(Boolean, default=False)
    large_img = Column(String, nullable=True)
    location_found = Column(String, nullable=True)
    manufacturer_name = Column(String, nullable=True)
    external_id = Column(String, nullable=True)
    registry_name = Column(String, nullable=True)
    registry_url = Column(String, nullable=True)
    serial = Column(String, nullable=True)
    status = Column(String, nullable=True)
    stolen = Column(Boolean, default=False)
    stolen_coordinates = Column(String, nullable=True)
    stolen_location = Column(String, nullable=True)
    thumb = Column(String, nullable=True)
    title = Column(String, nullable=True)
    url = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    
