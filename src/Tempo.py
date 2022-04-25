import time

class Tempo: 

    def __init__(self): 
        self.tempo_inicial = time.time()

    def get_tempo_final(self):
        return time.time() - self.tempo_inicial