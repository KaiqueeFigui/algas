import time
import sys
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel
from database.Connection import Connection

session = Connection().session

def contador_tempo_memoria(inicio, fim, passo = 1):
    valida_range(inicio, fim, passo)
    start = time.time()
    Range = select_range(inicio, fim, passo)
    transactions = []
    espaco = []
    for i in range(inicio, fim, passo):
        transactions.append(i)
        espaco.append(sys.getsizeof(i))
        
    for i in range(0, len(transactions), 1):
        Transaction = TransactionModel(espaco = espaco[i], passo = transactions[i], fk_range = Range.id)
        session.add(Transaction)
        session.commit()
        print("Transaction: ", transactions[i], " - Memory: ", espaco[i])
    Range.tempo = time.time() - start
    session.add(Range)
    session.commit()
    print("Tempo total: ", Range.tempo)

def select_range(inicio, fim, passo):
    range = session.query(RangeModel).filter_by(inicio = inicio, fim = fim, passo = passo).first()
    if (range == None):
        Range = RangeModel(inicio = inicio, fim = fim, passo = passo)
        session.add(Range)
        session.commit()
        return Range
    else:
        return range

def valida_range(inicio, fim, passo):
    if fim < inicio and passo > -1:
        raise Exception("O passo deve ser negativo para fazer inserção no banco")

    if passo == 0:
        raise Exception("O passo tem que ser maior que zero")

    if inicio == fim:
        raise Exception("Inicio e fim devem ser diferentes para haver um intrvalo")
    
    subtract = fim - inicio
    if passo > subtract:
        raise Exception("O passo deve ser menor para haver uma transação")

print("Escolha o início do range")
questionStart = int(input())
print("Escolha o fim do range")
questionFinal = int(input())
print("Escolha o passo do range")
questionStep = int(input())

contador_tempo_memoria(questionStart, questionFinal, questionStep)