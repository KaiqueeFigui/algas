from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class NatureModel(Base):

    __tablename__ = 'natures'

    id = Column(Integer, primary_key=True)
    initials = Column(String)
    nature_description = Column(String)