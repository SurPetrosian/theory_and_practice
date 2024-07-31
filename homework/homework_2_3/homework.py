import json
import random


class Question:
    def __init__(self, text_question, complexity, right_answer):
        self.text_question = text_question
        self.complexity = complexity
        self.right_answer = right_answer
        self.as_question = False
        self.user_answer = None
        self.points = complexity * 10

    def get_points(self):  # Возвращает int, количество баллов. Баллы зависят от сложности: за 1 дается 10 баллов,
        # за 5 дается 50 баллов.
        return self.points

    def is_correct(self):  # Возвращает True, если ответ пользователя совпадает с верным ответом иначе False.
        if self.user_answer == self.right_answer:
            return True
        return False

    def build_question(self):
        return f'Вопрос: {self.text_question}\nСложность: {self.complexity}/5'

    """Возвращает вопрос в понятном пользователю виде, например:
    Вопрос: What do people often call American flag?
    Сложность 4/5
    """

    def build_positive_feedback(self):
        self.as_question = True
        if self.is_correct():
            return f'Ответ верный, получено {self.points} баллов'
        return f'Ответ неверный, верный ответ {self.right_answer}'


def question():
    file = open("questions.json", "r", encoding="utf-8")
    data = json.load(file)
    questions = []
    for i in data:
        questions.append(Question(i['q'], int(i['d']), i['a']))
    return questions


def statistic(list_):
    points = 0
    total_answers = 0
    for item in list_:
        if item.is_correct():
            points += item.points
            total_answers +=1
    return f'Вот и все\nОтвечено {total_answers} вопроса из 5\nНабрано баллов: {points}'


def main():
    print('Игра начинается!')
    questions = question()
    random.shuffle(questions)

    for quest in questions:
        print(quest.build_question())
        answer = input()
        quest.user_answer = answer
        print(quest.build_positive_feedback())

    print(statistic(questions))


main()
