from unittest import IsolatedAsyncioTestCase
from module import AccentsQuiz

# TODO: fix relative import
class TestAccentsQuiz(IsolatedAsyncioTestCase):
	async def test_get_question(self):
		quiz = AccentsQuiz()
		for _ in range(10000):
			question = await quiz.get_question()
			if len(question.answer) <= 3:
				self.fail(f"question.answer <= 3, wrong word ({question.answer})")
			if len(question.options) > quiz.max_options:
				self.fail(f"question options > quiz.max_options: {question.options}")

	async def test_get_questions(self):
		# TODO: COMPLETE
		self.fail()
