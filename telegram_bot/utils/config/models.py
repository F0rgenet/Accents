from dataclasses import dataclass

@dataclass()
class ConfigData(object):
	token: str = ""
	pablo: str = ""

	def __str__(self):
		return f"AccentsBotConfig"