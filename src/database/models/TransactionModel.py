import datetime
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TransactionModel(Base):

    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    transaction_date = Column(DateTime, default=datetime.datetime.utcnow)
    transaction_value = Column(Float)
    fk_nature = Column(Integer)