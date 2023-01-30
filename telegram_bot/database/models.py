from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .main import Database


class User(Database.BASE):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	telegram_id = Column(Integer, nullable=False)
	username = Column(String, nullable=False)
	solved_tasks = Column(Integer, default=0)
	solved_correctly = Column(Integer, default=0)


def register_models():
	Database.BASE.metadata.create_all(Database().engine)
