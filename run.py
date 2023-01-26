import asyncio

from quiz import AccentsQuiz
from quiz.models import Question

async def test():
	quiz = AccentsQuiz()
	questions: list[Question] = await quiz.get_questions(int(input("Введите количество вопросов: ")))
	right_answers = 0
	for question in questions:
		options = ", ".join(question.options)
		context = ""
		if question.context:
			context = f"\n{question.context}"
		print(f"Выберите верное ударение:\n{options}{context}")
		index = int(input())-1
		if index == question.answer_index:
			print(f"Совершенно верно! Ответ: {question.answer}")
			right_answers += 1
		else:
			print(f"Неправильный вариант! Ответ: {question.answer}")
	print(f"Ваш результат: {right_answers}/{len(questions)} ({round(right_answers/len(questions) * 100, 2)}%)")

def main():
	asyncio.run(test())


if __name__ == '__main__':
	main()
