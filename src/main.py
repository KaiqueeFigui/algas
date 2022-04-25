import random
from datetime import date
from database.models.NatureModel import NatureModel
from database.Connection import Connection
from tqdm import tqdm

session = Connection().session
natures = ["G2G", "G2B", "G2P", "B2G", "P2G", "B2B", "B2P", "P2B", "P2P"]

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