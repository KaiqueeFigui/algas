from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class RangeModel(Base):

    __tablename__ = 'ranges'

    id = Column(Integer, primary_key=True)
    inicio = Column(Integer)
    fim = Column(Integer)
    passo = Column(Integer)