from dataclasses import dataclass
import random


@dataclass
class Question(object):
	options: list
	answer: str


class DataManager(object):
	def __init__(self):
		with open("../data/accents.txt", "r", encoding="UTF-8") as file:
			raw = [line.replace("\n", "") for line in file.readlines() if not line.startswith("#")]
			self.accents = [elem for elem in " ".join(raw).split(" ") if elem]

	def get_data(self):
		pass

class AccentsQuiz(object):
	def __init__(self, max_options: int = 3):
		manager = DataManager()
		manager.get_data()

		self.max_options = max_options
		self.vowels = "аеёиоэюяуы"

	async def get_question(self):
		word: str = random.choice(self.accents)
		answer = word

		word = word.lower()
		options = []
		for i, letter in enumerate(word):
			if letter not in self.vowels:
				continue
			option = word[:i]+letter.upper()+word[i + 1: len(word)+1]
			if option != answer:
				options.append(option)

		options = options[:self.max_options - 1]
		options.append(answer)
		random.shuffle(options)
		return Question(options, answer)

	async def get_questions(self, count: int):
		questions = []
		while len(questions) < count:
			question = await self.get_question()
			if question not in questions:
				questions.append(question)

		return questions
