from configparser import ConfigParser, ParsingError
from .models import ConfigData
from dataclasses import asdict
from loguru import logger

# TODO: fix

class BotConfig(object):
	def __init__(self, file_path: str):
		self.config = ConfigParser()
		self.model = ConfigData()
		self.section = str(self.model)

		self.file_path = file_path
		if not self.check_config():
			self.create_config_file()

	def get_data(self):
		return {data[0]: data[1] for data in self.config.items(self.section)}

	def check_config(self):
		model_fields = list(asdict(self.model).keys())
		checked = []
		try:
			open(self.file_path)
		except FileNotFoundError:
			logger.warning(f"Файла конфига не существует по пути {self.file_path}")
			return False

		try:
			self.config.read(self.file_path, encoding="UTF-8")
		except ParsingError as exception:
			logger.warning(f"Файл конфига повреждён: {exception}")
			return False
		if self.section not in self.config.sections():
			logger.warning(f"Секция отсутствует в файле конфига: {self.section}")
			return False
		config_fields = self.config.options(self.section)
		for field in config_fields:
			if field not in model_fields:
				logger.warning(f"Поле {field} отсутствует в модели, поля модели: {model_fields}")
				return False
			checked.append(field)
		if model_fields != checked:
			logger.warning(f"Поля конфига не совпали с полями модели: {checked}/{model_fields}")
			return False
		logger.info("Файл конфигурации бота проверен")
		return True

	def create_config_file(self):
		if self.section not in self.config.sections():
			self.config.add_section(self.section)
		with open(self.file_path, "w", encoding="UTF-8") as file:
			self.config.write(file)
