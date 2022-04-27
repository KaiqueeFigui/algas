from database.models.TransactionModel import TransactionModel
from database.models.TaxaCreditoModel import TaxaCreditoModel
from database.Connection import Connection
import random
import sys
from datetime import date
from Tempo import Tempo

session = Connection().session

segmento = ["Varejo", "Agronegócio", "Suprimentos", "Drogaria"]

def insert_transaction(Transaction, espaco, tempo):
    Transaction.espaco = espaco
    Transaction.tempo = tempo
    session.add(Transaction)
    session.commit()
    session.refresh(Transaction)
    return Transaction

def gerar_dados(inicio, fim):
    tempo = Tempo()
    random_data = gerar_random() 
    TaxaCredito = TaxaCreditoModel(data_inicio = inicio, data_fim = fim, segmento = random_data["segmento"], taxa_mes = random_data["taxa_mes"], taxa_ano = random_data["taxa_ano"], risco = random_data["risco"], valor = random_data["valor"])
    Transaction = insert_transaction(TransactionModel(), sys.getsizeof(TaxaCredito), None)
    TaxaCredito.fk_transaction = Transaction.id
    session.add(TaxaCredito)
    session.commit()
    insert_transaction(Transaction, sys.getsizeof(TaxaCredito), tempo.get_tempo_final())

def gerar_random():
    index_segmento = random.randrange(0, 4)
    risco = (random.randrange(1, 100)) / 100
    valor = round(random.uniform(100_000, 500_000_000), 2)
    taxa_mes = random.randrange(1, 20)
    taxa_ano = random.randrange(1, 99)
    taxa_mes += taxa_mes * risco
    taxa_ano += taxa_ano * risco
    return {"segmento": segmento[index_segmento], "taxa_mes": taxa_mes, "taxa_ano": taxa_ano, "risco": risco, "valor": valor}

    
def dif_meses(data_inicial, data_final):
    return (data_inicial.year - data_final.year) * 12 + data_inicial.month - data_final.month

def main():
    print("Digite a data de inicio no formato YYYY-MM-DD:")
    data_inicio = date.fromisoformat(input())
    print("Digite a data final no formato YYYY-MM-DD:")
    data_final = date.fromisoformat(input())

    dif = dif_meses(data_final, data_inicio)
    for _ in range(0, dif):
        gerar_dados(data_inicio, data_final) 

main()