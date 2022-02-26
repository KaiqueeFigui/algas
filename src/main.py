import time
import sys
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "algas",
    auth_plugin='mysql_native_password'
)

cursor = banco.cursor()

def contador_tempo_memoria(inicio, fim, passo = 1):
    start = time.time()
    transactions = []
    memoria_usada = []
    for i in range(inicio, fim, passo):
        transactions.append(i)
        memoria_usada.append(sys.getsizeof(transactions))
    tempo = (time.time() - start)
    return { 'inicio': inicio, 'fim': fim, 'passo': passo, 'transactions': transactions, 'tempo': tempo, 'memoria_usada': memoria_usada }

def salva_valores_bd(valores):
    query = "INSERT INTO algas (inicio, fim, passo, valor, tempo, memoria_usada) VALUES (%s, %s, %s, %s, %s, %s)"
    transactions = valores['transactions']
    tempo = valores['tempo']
    memoria_usada = valores['memoria_usada']

    for i in range(0, len(transactions)):
        info = (valores['inicio'], valores['fim'], valores['passo'], transactions[i], tempo, memoria_usada[i])
        cursor.execute(query, info)
    banco.commit()
    print(cursor.rowcount)

salva_valores_bd(contador_tempo_memoria(1, 100000, 1000))