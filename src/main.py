import random
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel
from database.Connection import Connection

session = Connection().session

def generate_random_transactions(year):
    verifyIfYearExistsInDatabase = session.query(TransactionModel).filter_by(year = year).first()

    if (verifyIfYearExistsInDatabase == None):
        for i in range(1, 5):
            value = random.randint(300000000, 798061937)

            if i == 4:
                value = random.randint(600000000, 1098061937)
            
            Transaction = TransactionModel(year = year, description = str(year) + '-T' + str(i), value = value)
            session.add(Transaction)
            session.commit()
            print("Ano: ", transaction.year, "Ano/Trimestre ", transaction.description, " - Valor: ", transaction.value)
    else:
        print("\n")
        transactionsExists = session.query(TransactionModel).filter_by(year = year).all()

        for transaction in transactionsExists:
            print("Ano: ", transaction.year, "Ano/Trimestre ", transaction.description, " - Valor: ", transaction.value)

def generate_random_transactions_last_10_years():
    for year in range(2022, 2022 - 10, -1):
        generate_random_transactions(year)

def get_all_transactions():
    transactions = session.query(TransactionModel).all()

    if len(transactions) == 0:
        print("Nenhuma transação encontrada")
    else:
        print("\nTransações encontradas:\n")
        for transaction in transactions:
            print("Ano: ", transaction.year, "Ano/Trimestre ", transaction.description, " - Valor: ", transaction.value)

def main():
    print("Escolha a opção desejada:\n")
    print("1 - Gerar transações aleatórias de um ano específico")
    print("2 - Gerar transações aleatórias dos últimos 10 anos")
    print("3 - Obter todas as transações armanezadas no banco de dados")
    print("4 - Sair")

    optionSelected = int(input())
    switchOption(optionSelected)

def switchOption(optionSelected):
    if optionSelected == 1:
        year = int(input("Digite o ano desejado: "))
        generate_random_transactions(year)
    elif optionSelected == 2:
        generate_random_transactions_last_10_years()
    elif optionSelected == 3:
        get_all_transactions()
    elif optionSelected == 4:
        print("Saindo...")
        exit()
    else:
        print("Opção inválida")

main()