import time
import sys
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "algas",
    password = "12345",
    database = "algas",
    auth_plugin='mysql_native_password'
)

cursor = banco.cursor()

def contador_tempo_memoria(inicio, fim, passo = 1):
    id_range = select_id_range(inicio, fim)
    transactions = []
    espaco = []
    start = time.time()
    for i in range(inicio, fim, passo):
        transactions.append(i)
        espaco.append(sys.getsizeof(i))

    for i in range(0, len(transactions), 1):
        save_transactions((time.time() - start), espaco[i], transactions[i], id_range)

def select_id_range(inicio, fim):
    query = "SELECT ID from ranges WHERE inicio = %s AND fim = %s"
    cursor.execute(query, (inicio, fim))
    id_range = cursor.fetchone()[0]
    return id_range
        

def save_transactions(tempo, espaco, passo, id_range):
    query = "INSERT INTO transactions (tempo, espaco, passo, fk_range) VALUES (%s, %s, %s, %s)"
    info = (tempo, espaco, passo, id_range)
    cursor.execute(query, info)
    banco.commit()
    print(cursor.rowcount)

contador_tempo_memoria(100000, 600000, 100000)
contador_tempo_memoria(1000, 6000, 100)
contador_tempo_memoria(100, 600, 100)
contador_tempo_memoria(10, 60, 10)
contador_tempo_memoria(1000000, 6000000, 1000000)