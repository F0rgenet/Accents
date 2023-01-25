import asyncio

from quiz.module import AccentsQuiz


async def test():
	quiz = AccentsQuiz()
	for _ in range(20):
		question = await quiz.get_question()
		print(question)

def main():
	asyncio.run(test())


if __name__ == '__main__':
	main()
