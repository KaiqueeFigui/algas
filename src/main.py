import time
import sys
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel
from database.Connection import Connection
from sqlalchemy.orm import sessionmaker

session = Connection().session

def contador_tempo_memoria(inicio, fim, passo = 1):
    id_range = session.query(RangeModel).filter_by(inicio = inicio, fim = fim).first().id
    transactions = []
    espaco = []
    start = time.time()
    for i in range(inicio, fim, passo):
        transactions.append(i)
        espaco.append(sys.getsizeof(i))
        
    for i in range(0, len(transactions), 1):
        Transaction = TransactionModel(tempo = time.time() - start, espaco = espaco[i], passo = transactions[i], fk_range = id_range)
        session.add(Transaction)
        session.commit()

contador_tempo_memoria(100000, 600000, 100000)
contador_tempo_memoria(1000, 6000, 100)
contador_tempo_memoria(100, 600, 100)
contador_tempo_memoria(10, 60, 10)
contador_tempo_memoria(1000000, 6000000, 1000000)