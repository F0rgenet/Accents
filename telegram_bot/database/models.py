from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .main import Database


class User(Database.BASE):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	telegram_id = Column(Integer, nullable=False)


def register_models():
	Database.BASE.metadata.create_all(Database().engine)
