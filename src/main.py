import time
import sys
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "kaique",
    password = "12345",
    database = "algas",
    auth_plugin='mysql_native_password'
)

cursor = banco.cursor()

def contador_tempo_memoria(inicio, fim, passo = 1):
    transactions = []
    tempo = []
    memoria_usada = []
    for i in range(inicio, fim, passo):
        start = time.time()
        transactions.append(i)
        tempo.append(time.time() - start)
        memoria_usada.append(sys.getsizeof(transactions))
    return { 'inicio': inicio, 'fim': fim, 'passo': passo, 'transactions': transactions, 'tempo': tempo, 'memoria_usada': memoria_usada }

def salva_valores_bd(valores):
    query = "INSERT INTO algas (inicio, fim, passo, valor, tempo, memoria_usada) VALUES (%s, %s, %s, %s, %s, %s)"
    transactions = valores['transactions']
    tempo = valores['tempo']
    memoria_usada = valores['memoria_usada']

    for i in range(0, len(transactions)):
        info = (valores['inicio'], valores['fim'], valores['passo'], transactions[i], tempo[i], memoria_usada[i])
        cursor.execute(query, info)
    banco.commit()
    print(cursor.rowcount)

salva_valores_bd(contador_tempo_memoria(1, 10, 1))