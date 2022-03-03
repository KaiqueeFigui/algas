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
    for i in range(inicio, fim, passo):
        transactions.append(i)
    memoria_usada = sys.getsizeof(transactions)
    tempo = (time.time() - start)
    return { 'inicio': inicio, 'fim': fim, 'passo': passo, 'tempo': tempo, 'memoria_usada': memoria_usada }

def salva_valores_bd(valores):
    query = "INSERT INTO algas (inicio, fim, passo, tempo, memoria_usada) VALUES (%s, %s, %s, %s, %s)"
    tempo = valores['tempo']
    memoria_usada = valores['memoria_usada']
    info = (valores['inicio'], valores['fim'], valores['passo'], tempo, memoria_usada)
    cursor.execute(query, info)
    banco.commit()
    print(cursor.rowcount)

salva_valores_bd(contador_tempo_memoria(100000, 600000, 100000))
salva_valores_bd(contador_tempo_memoria(1000, 6000, 100))
salva_valores_bd(contador_tempo_memoria(100, 600, 100))
salva_valores_bd(contador_tempo_memoria(10, 60, 10))
salva_valores_bd(contador_tempo_memoria(1000000, 6000000, 1000000))