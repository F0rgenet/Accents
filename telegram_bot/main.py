from loguru import logger

from aiogram import Bot, Dispatcher, executor
from telegram_bot.database import register_models
from telegram_bot.utils import BotConfig

async def __on_startup(dispatcher: Dispatcher):
	register_models()

	logger.info("Бот запущен")

def startup():
	config = BotConfig("telegram_bot/config.ini")
	print(config.get_data()["token"])
