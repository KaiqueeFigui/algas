import time
import sys
import random
from datetime import date
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel
from database.models.NatureModel import NatureModel
from database.Connection import Connection
from tqdm import tqdm

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

def gera_valores_por_natureza(data, natureza, quantidade):
    for i in tqdm(range(0, quantidade), desc='Processando dados'):
        random_transaction = round(random.uniform(1, 10_000), 2)
        Nature = NatureModel(date = data, value = random_transaction, nature_type = natureza)
        session.add(Nature)
        session.commit()

def resgata_natureza(indice):
    if indice == 1:
        return "G2G"
    elif indice == 2:
        return "G2B"
    elif indice == 3:
        return "G2P"
    elif indice == 4:
        return "B2G"
    elif indice == 5:
        return "P2G"
    elif indice == 6:
        return "B2B"
    elif indice == 7:
        return "B2P"
    elif indice == 8:
        return "P2B"
    elif indice == 9:
        return "P2P"

print("Digite a data no formato YYYY-MM-DD:")
date_transaction = date.fromisoformat(input())
print("\nEscolha a natureza: \n1 - G2G \n2 - G2B \n3 - G2P \n4 - B2G \n5 - P2G \n6 - B2B \n7 - B2P \n8 - P2B \n9 - P2P")
nature_transaction = resgata_natureza(int(input()))
print("\nDigite a quantidade de transações:")
count_transactions = int(input())
print("\n")

gera_valores_por_natureza(date_transaction, nature_transaction, count_transactions)