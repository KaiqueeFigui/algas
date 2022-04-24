import time
import sys
import random
from datetime import date
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel
from database.models.NatureModel import NatureModel
from database.models.RegionModel import RegionModel
from database.Connection import Connection
from tqdm import tqdm

session = Connection().session
natures = ["G2G", "G2B", "G2P", "B2G", "P2G", "B2B", "B2P", "P2B", "P2P"]

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

def gera_valores_por_natureza(data, passo):
    for nature in range(0, len(natures)):
        for i in tqdm(range(0, ((nature + 1) * passo)), desc='Processando dados ' + natures[nature]):
            random_transaction = round(random.uniform(1, 10_000), 2)
            Nature = NatureModel(date = data, value = random_transaction, nature_type = natures[nature])
            session.add(Nature)
            session.commit()

print("Digite a data no formato YYYY-MM-DD:")
date_transaction = date.fromisoformat(input())
print("\nDigite o quantidade de passos por natureza:")
pass_count = int(input())
print("\n")

gera_valores_por_natureza(date_transaction, pass_count)