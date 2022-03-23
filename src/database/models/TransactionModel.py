from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from .RangeModel import RangeModel

Base = declarative_base()

class TransactionModel(Base):

    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    tempo = Column(Float)
    espaco = Column(Integer)
    passo = Column(Integer)
    fk_range = Column(Integer)