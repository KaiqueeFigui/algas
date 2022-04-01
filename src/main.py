import time
import sys
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel
from database.Connection import Connection
from sqlalchemy.orm import sessionmaker

session = Connection().session

def contador_tempo_memoria(inicio, fim, passo = 1):
    Range = select_range(inicio, fim, passo)
    transactions = []
    espaco = []
    start = time.time()
    for i in range(inicio, fim, passo):
        transactions.append(i)
        espaco.append(sys.getsizeof(i))
        
    for i in range(0, len(transactions), 1):
        Transaction = TransactionModel(tempo = time.time() - start, espaco = espaco[i], passo = transactions[i], fk_range = Range.id)
        session.add(Transaction)
        session.commit()
        print("Transaction: ", transactions[i], " - Memory: ", espaco[i])

def select_range(inicio, fim, passo):
    range = session.query(RangeModel).filter_by(inicio = inicio, fim = fim, passo = passo).first()
    if (range == None):
        Range = RangeModel(inicio = inicio, fim = fim, passo = passo)
        session.add(Range)
        session.commit()
        return Range
    else:
        return range

print("Escolha o início do range")
questionStart = int(input())
print("Escolha o fim do range")
questionFinal = int(input())
print("Escolha o passo do range")
questionStep = int(input())

contador_tempo_memoria(questionStart, questionFinal, questionStep)