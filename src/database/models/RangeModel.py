from .BaseModel import BaseModel

class RangeModel(BaseModel):
    def __init__(self):
        self.table_name = "ranges"
        self.fields = ['id', 'inicio', 'fim']
        super().__init__(self.table_name, self.fields)