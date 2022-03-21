from .BaseModel import BaseModel

class TransactionModel(BaseModel):
    def __init__(self):
        self.table_name = 'transactions'
        self.fields = ['id', 'tempo', 'espaco', 'passo', 'fk_range']
        super().__init__(self.table_name, self.fields)