from dataclasses import dataclass


@dataclass()
class Question(object):
	options: list
	answer_index: int
	answer: str
	context: str = None

@dataclass()
class Word(object):
	content: str
	context: str = None


@dataclass()
class Category(object):
	name: str
	title: str
