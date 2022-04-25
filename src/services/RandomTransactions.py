import random
import time
import sys
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel
from database.Connection import Connection

session = Connection().session

def generate_random_transactions(year):
    start_time = time.time()
    used_space = []
    verifyIfYearExistsInDatabase = session.query(TransactionModel).filter_by(year = year).first()

    if (verifyIfYearExistsInDatabase == None):
        for i in range(0, 4):
            value = round(random.uniform(300000000.00, 600000000.99), 2)
            used_space.append(sys.getsizeof(i))

            if i == 3:  
                value = round(random.uniform(600000000.00, 1000000000.99), 2)
            
            value = str(value)        
            Transaction = TransactionModel(year = year, description = str(year) + '-T' + str(i + 1), value = value.replace('.', ','), space = used_space[i], time = time.time() - start_time)  
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