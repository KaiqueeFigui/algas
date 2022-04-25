import random
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel
from database.Connection import Connection

session = Connection().session

def generate_random_transactions(year):
    verifyIfYearExistsInDatabase = session.query(TransactionModel).filter_by(year = year).first()

    if (verifyIfYearExistsInDatabase == None):
        for i in range(0, 4):
            value = random.randint(300000000, 798061937)

            if i == 3:
                 value = random.randint(600000000, 1098061937)
                
            Transaction = TransactionModel(year = year, description = str(year) + '-T' + str(i + 1), value = value)
            session.add(Transaction)
            session.commit()
            print("Ano: ", Transaction.year, "Ano/Trimestre ", Transaction.description, " - Valor: ", Transaction.value)
    else:
            print("\n")
            transactionsExists = session.query(TransactionModel).filter_by(year = year).all()
            
            for transaction in transactionsExists:
                print("Ano: ", transaction.year, "Ano/Trimestre ", transaction.description, " - Valor: ", transaction.value)

def generate_random_transactions_last_10_years():
    for year in range(2022, 2022 - 10, -1):
        generate_random_transactions(year)