from sqlalchemy.exc import NoResultFound

from loguru import logger

from telegram_bot.database.main import Database
from telegram_bot.database.models import User


async def create_user(telegram_id: int):
	session = Database().session
	try:
		session.query(User.telegram_id).filter(User.telegram_id == telegram_id).one()
	except NoResultFound:
		logger.info(f"В базу данных добавлен пользователь (id:{telegram_id})")
		session.add(User(telegram_id=telegram_id))
		session.commit()
