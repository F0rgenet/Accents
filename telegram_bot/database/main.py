from typing import Final

import sqlalchemy.orm
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from utils import SingletonMeta


class Database(metaclass=SingletonMeta):
    BASE: sqlalchemy.orm.DeclarativeBase = declarative_base()

    def __init__(self):
        self.__engine = create_engine('sqlite:///database.db')
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    @property
    def session(self):
        return self.__session

    @property
    def engine(self):
        return self.__engine
