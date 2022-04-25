import random
import sys
import time
from datetime import date
from database.models.TransactionModel import TransactionModel
from database.models.PerformanceModel import PerformanceModel
from database.models.NatureModel import NatureModel
from database.Connection import Connection
from tqdm import tqdm

session = Connection().session

def get_natures():
    natures = session.query(NatureModel).all()
    return natures

def generate_performance(start_time, memory_usage, nature_id):
    runtime = time.time() - start_time
    Performance = PerformanceModel(runtime = runtime, allocated_space = memory_usage, fk_nature = nature_id)
    session.add(Performance)
    session.commit()

def generate_values_by_nature(data, step):
    natures = get_natures()
    for nature in range(0, len(natures)):
        for _ in tqdm(range(0, ((nature + 1) * step)), desc='Processando dados ' + natures[nature].initials):
            start_time = time.time()
            random_transaction = round(random.uniform(1, 10_000), 2)
            Transaction = TransactionModel(transaction_date = data, transaction_value = random_transaction, fk_nature = natures[nature].id)
            session.add(Transaction)
            session.commit()
            generate_performance(start_time, sys.getsizeof(Transaction), natures[nature].id)

print("Digite a data no formato YYYY-MM-DD:")
date_transaction = date.fromisoformat(input())
print("\nDigite o quantidade de passos por natureza:")
step_count = int(input())
print("\n")

generate_values_by_nature(date_transaction, step_count)