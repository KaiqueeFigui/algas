import os
from dotenv import load_dotenv
import mysql.connector

class Connection:

    connection = {}
    database = {}

    def __init__(self):
        load_dotenv()
        self.connection = {
            "host": os.getenv('DATABASE_HOST'),
            "user": os.getenv('DATABASE_USER'),
            "password": os.getenv('DATABASE_PASSWORD'),
            "database": os.getenv('DATABASE_NAME'),
            "auth_plugin": 'mysql_native_password'
        }

    
    def open_connection(self):
        self.database = mysql.connector.connect(
            host = self.connection["host"],
            user = self.connection["user"],
            password = self.connection["password"],
            database = self.connection["database"],
            auth_plugin = self.connection["auth_plugin"]
        )
        return self.database

