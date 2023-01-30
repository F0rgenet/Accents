import sqlalchemy.orm.attributes

from telegram_bot.database.main import Database
from telegram_bot.database.models import User

async def get_leaderboard_data():
	users = Database().session.query(User).all()
	users.sort(key=lambda user: user.solved_correctly/user.solved_tasks)
	return users
