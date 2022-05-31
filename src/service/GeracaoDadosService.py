import time
import sys
from database.models.RangeModel import RangeModel
from database.models.TransactionModel import TransactionModel
from database.Connection import Connection


class GeracaoDadosService:

    def __int__(self):
        self.session = Connection().session

    def contador_tempo_memoria(self, inicio, fim, passo=1):
        self.__valida_range(inicio, fim, passo)
        start = time.time()
        Range = self.__select_range(inicio, fim, passo)
        transactions = []
        espaco = []
        for i in range(inicio, fim, passo):
            transactions.append(i)
            espaco.append(sys.getsizeof(i))

        for i in range(0, len(transactions), 1):
            Transaction = TransactionModel(espaco=espaco[i], passo=transactions[i], fk_range=Range.id)
            self.session.add(Transaction)
            self.session.commit()
            print("Transaction: ", transactions[i], " - Memory: ", espaco[i])
        Range.tempo = time.time() - start
        self.session.add(Range)
        self.session.commit()
        print("Tempo total: ", Range.tempo)

    def __select_range(self, inicio, fim, passo):
        range = self.session.query(RangeModel).filter_by(inicio=inicio, fim=fim, passo=passo).first()
        if (range == None):
            Range = RangeModel(inicio=inicio, fim=fim, passo=passo)
            self.session.add(Range)
            self.session.commit()
            return Range
        else:
            return range

    def __valida_range(self, inicio, fim, passo):
        if fim < inicio and passo > -1:
            raise Exception("O passo deve ser negativo para fazer inserção no banco")

        if passo == 0:
            raise Exception("O passo tem que ser maior que zero")

        if inicio == fim:
            raise Exception("Inicio e fim devem ser diferentes para haver um intrvalo")

        subtract = fim - inicio
        if passo > subtract:
            raise Exception("O passo deve ser menor para haver uma transação")

