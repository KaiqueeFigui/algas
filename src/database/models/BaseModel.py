from abc import ABC, abstractmethod
from database.Connection import Connection

class BaseModel(ABC):

    def __init__(self, table_name, fields):
        self.table_name = table_name
        self.fields = fields
        self.connection = Connection()

    def find_all(self):
        return self.connection.select_all(self.table_name)

    def find_by_id(self, id):
        return self.find_where(self.fields[self.fields.index('id')], '=', id)

    def find_where(self, field, operator, value):
        return self.connection.select_where(self.table_name, field, operator, value)

    def remove(self, id):
        return self.connection.delete_by_id(self.table_name, [id])

    def update(self, id, fields, values):
        return self.connection.update_by_id(self.table_name, fields, values, id)
    
    def save(self, values):
        fields_copy = self.fields.copy()
        fields_copy.remove('id')
        return self.connection.insert(self.table_name, fields_copy, values)
