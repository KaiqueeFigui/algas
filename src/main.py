from database.models.TransactionModel import TransactionModel
from database.models.TaxaCreditoModel import TaxaCreditoModel
from database.Connection import Connection
import random
import sys
from datetime import date
from Tempo import Tempo

session = Connection().session

segmento = ["Varejo", "Agronegócio", "Suprimentos", "Drogaria"]

def insert_transaction(espaco, tempo, fk_taxa):
    Transaction = TransactionModel(espaco = espaco, tempo = tempo, fk_taxa = fk_taxa)
    session.add(Transaction)
    session.commit()

def gerar_dados(inicio, fim):
    tempo = Tempo()
    random_data = gerar_random() 
    TaxaCredito = TaxaCreditoModel(data_inicio = inicio, data_fim = fim, segmento = random_data["segmento"], taxa_mes = random_data["taxa_mes"], taxa_ano = random_data["taxa_ano"])
    session.add(TaxaCredito)
    session.commit()
    insert_transaction(sys.getsizeof(TaxaCredito), (tempo.get_tempo_final()), TaxaCredito.id)

def gerar_random():
    index_segmento = random.randrange(0, 3)
    taxa_mes = random.randrange(6, 9) 
    taxa_ano = random.randrange(19, 22)
    return {"segmento": segmento[index_segmento], "taxa_mes": taxa_mes, "taxa_ano": taxa_ano}

def main():
    # print("Digite a data de inicio no formato YYYY-MM-DD:")
    # data_inicio = date.fromisoformat(input())
    # print("Digite a data final no formato YYYY-MM-DD:")
    # data_final = date.fromisoformat(input())
    data_inicio = "2021-12-01"
    data_final = "2022-01-01"


    for i in range(1, 100, 1):
        gerar_dados(data_inicio, data_final)

main()