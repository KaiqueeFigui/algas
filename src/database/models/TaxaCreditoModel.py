from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class TaxaCreditoModel(Base):

    __tablename__ = 'taxa_credito'

    id = Column(Integer, primary_key=True)
    data_inicio = Column(DateTime, default=datetime.datetime.utcnow)
    data_fim = Column(DateTime, default=datetime.datetime.utcnow)
    segmento = Column(String)
    risco = Column(Float)
    valor = Column(Float)
    taxa_mes = Column(Float)
    taxa_ano = Column(Float)    
    fk_transaction = Column(Integer)
