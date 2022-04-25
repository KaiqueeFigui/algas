from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import declarative_base
from .RangeModel import RangeModel

Base = declarative_base()

class TransactionModel(Base):

    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    espaco = Column(Integer)
    tempo = Column(Float)
    fk_taxa = Column(Integer)