import random
import os

from typing import Literal

from utils.quiz.models import Question, Word, Category
from xml.etree import ElementTree


class XMLAccentsManager(object):
	# TODO: xml append/remove
	def __init__(self):
		self.categories = []
		self.words = {}

		self.parse()

	def parse(self):
		self.categories = []
		self.words = {}

		root = ElementTree.parse("../../data/accents.xml").getroot()
		# TODO: config for path?
		for xml_category in root:
			self.categories.append(Category(xml_category.tag, xml_category.attrib["title"]))
			self.words[xml_category.tag] = []

			for word in xml_category:
				context = None
				if "context" in word.attrib:
					context = word.attrib["context"]
				data = Word(word.text, context)
				self.words[xml_category.tag].append(data)

	async def get_list(self, categories: Literal["all"] | list[str] = "all"):
		result = []
		for category, words in self.words.items():
			if categories == "all" or category in categories:
				result.extend(words)
		return result

class AccentsQuiz(object):
	def __init__(self, max_options: int = 3):
		self.manager = XMLAccentsManager()

		self.max_options = max_options
		self.vowels = "аеёиоэюяуы"

	@staticmethod
	async def check_answer(question: Question, chosen_index: int):
		if chosen_index == question.answer_index:
			return True
		return False

	async def get_question(self, categories: Literal["all"] | list[str] = "all"):
		words = await self.manager.get_list(categories)
		word: Word = random.choice(words)

		answer = word.content

		symbols = word.content.lower().replace("ё", "е")
		options = []
		for i, letter in enumerate(symbols):
			if letter not in self.vowels:
				continue
			option = symbols[:i]+letter.upper()+symbols[i + 1: len(symbols)+1]
			if option != answer:
				options.append(option)

		options = options[:self.max_options - 1]
		answer_option = answer.replace("Ё", "Е")
		options.append(answer_option)
		random.shuffle(options)
		answer_index = options.index(answer_option)
		return Question(options, answer_index, answer, word.context)

	async def get_questions(self, count: int, categories: Literal["all"] | list[str] = "all"):
		# TODO: count > len(available_questions)
		questions = []
		while len(questions) < count:
			question = await self.get_question(categories)
			if question not in questions:
				questions.append(question)

		return questions
