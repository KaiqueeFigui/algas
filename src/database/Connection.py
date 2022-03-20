import os
from dotenv import load_dotenv
import mysql.connector

class Connection:

    def __init__(self):
        load_dotenv()
        self.connection = {
            "host": os.getenv('DATABASE_HOST'),
            "user": os.getenv('DATABASE_USER'),
            "password": os.getenv('DATABASE_PASSWORD'),
            "database": os.getenv('DATABASE_NAME'),
            "auth_plugin": 'mysql_native_password'
        }
        self.connect()
    
    def connect(self):
        self.database = mysql.connector.connect(
            host = self.connection["host"],
            user = self.connection["user"],
            password = self.connection["password"],
            database = self.connection["database"],
            auth_plugin = self.connection["auth_plugin"]
        )
        return True

    def close(self):
        if self.database:
            self.database.close()
            return True

    def insert(self, table_name, fields, values):
        fommated_fields = ", ".join(fields)        
        values_placeholders = self.__get_values_placeholder(values)
        query = f"INSERT INTO {table_name} ({fommated_fields}) VALUES ({values_placeholders})" 
        self.__cursor_commit(query, values)

    def delete_by_id(self, table_name, id):
        query = f"DELETE FROM {table_name} WHERE id = %s"
        self.__cursor_commit(query, id)
        return True

    def update_by_id(self, table_name, fields, values, id):
        for j in range(len(values)):
            values[j] = '"' + values[j] + '"'
        for i in range(len(fields)):
            fields[i] += f" = {values[i]}"
        valuesToUpdate = ", ".join(fields)
        query = f"UPDATE {table_name} SET {valuesToUpdate} where id = {id}"
        self.__cursor_commit(query, None)
    
    def select_where(self, table_name, field, operator, value):
        if isinstance(value, str):
            value = '"' + value + '"'
        query = f"SELECT * FROM {table_name} WHERE {field} {operator} {value}"
        return self.__cursor_fetch_all(query)

    def select_all(self, table_name):
        query = 'SELECT * FROM {}'.format(table_name);
        return self.__cursor_fetch_all(query)

    def do_select(self, query):
        return self.__cursor_fetch_all(query)

    def __cursor_fetch_all(self, query):
        cursor = self.database.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data

    def __cursor_commit(self, query, values):
        cursor = self.database.cursor()
        if values is None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)
        cursor.close()
        self.__commit()

    def __get_values_placeholder(self, values: tuple):
        valuesPlaceholders = []
        for i in range(len(values)):
            valuesPlaceholders.append("%s")
        formatted_values = ", ".join(valuesPlaceholders)
        return formatted_values
    
    def __commit(self):
        self.database.commit()

    def __get_last_insert(self, cursor):
        id = cursor.lastrowid
        query = f"SELECT * FROM {table_name} WHERE id = {id}"
        cursor.execute(query)
        return cursor.fetchone()