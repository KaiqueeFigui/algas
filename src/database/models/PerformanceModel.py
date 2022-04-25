from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PerformanceModel(Base):

    __tablename__ = 'performance'

    id = Column(Integer, primary_key=True)
    runtime = Column(Float)
    allocated_space = Column(Integer)
    fk_nature = Column(Integer)