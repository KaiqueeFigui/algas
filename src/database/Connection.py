import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

class Connection():
    load_dotenv()
    os.getenv('')
    def __init__(self):
        user = os.getenv('DATABASE_USER')
        host = os.getenv('DATABASE_HOST')
        password = os.getenv('DATABASE_PASSWORD')
        database = os.getenv('DATABASE_NAME')
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}', echo = True)
        self.connection = self.engine.connect()
        self.__create_session()

    def __create_session(self):
        Session = sessionmaker(bind = self.engine)
        self.session = Session()