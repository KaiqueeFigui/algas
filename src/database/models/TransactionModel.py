from sqlalchemy import Column, Integer, String, Float, Numeric
from sqlalchemy.orm import declarative_base
from .RangeModel import RangeModel

Base = declarative_base()

class TransactionModel(Base):

    __tablename__ = 'transactions_with_card'

    id = Column(Integer, primary_key=True)
    year = Column(String)
    description = Column(String)
    value = Column(Numeric)