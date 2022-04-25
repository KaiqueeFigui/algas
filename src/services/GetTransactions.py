from database.models.TransactionModel import TransactionModel
from database.Connection import Connection

session = Connection().session

def get_all_transactions():
    transactions = session.query(TransactionModel).all()

    if len(transactions) == 0:
        print("Nenhuma transação encontrada")
        
    else:
        print("\nTransações encontradas:\n")
        for transaction in transactions:
            print("Ano: ", transaction.year, "Ano/Trimestre ", transaction.description, " - Valor: ", transaction.value)