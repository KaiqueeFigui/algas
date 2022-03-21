import time
import sys
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel

rangeModel = RangeModel()
transactionModel = TransactionModel()

def contador_tempo_memoria(inicio, fim, passo = 1):
    id_range = transactionModel.custom_find(f"SELECT id from ranges where inicio = {inicio} AND fim = {fim}")[0][0]
    transactions = []
    espaco = []
    start = time.time()
    for i in range(inicio, fim, passo):
        transactions.append(i)
        espaco.append(sys.getsizeof(i))
        
    for i in range(0, len(transactions), 1):
        transactionModel.save((time.time() - start, espaco[i], transactions[i], id_range))

contador_tempo_memoria(100000, 600000, 100000)
contador_tempo_memoria(1000, 6000, 100)
contador_tempo_memoria(100, 600, 100)
contador_tempo_memoria(10, 60, 10)
contador_tempo_memoria(1000000, 6000000, 1000000)