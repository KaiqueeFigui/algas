import datetime
from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RegionModel(Base):

    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    value = Column(Float)
    region = Column(String)
