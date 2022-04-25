from services.RandomTransactions import generate_random_transactions
from services.RandomTransactions import generate_random_transactions_last_10_years
from services.GetTransactions import get_all_transactions

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
