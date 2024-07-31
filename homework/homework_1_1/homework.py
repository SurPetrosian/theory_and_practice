question_1 = 'My name ___ Vova.'
question_2 = 'I ___ a coder'
question_3 = 'I live ___ Moscow.'

answer_1 = 'is'
answer_2 = 'am'
answer_3 = 'in'

user_name = input(
    '''Привет! Предлагаю проверить свои знания английского!
Напиши, как тебя зовут ''')

print(f'Привет, {user_name} начинаем тренировку!')
right_answer = 0
count = 0
user_input = input(question_1)
if user_input == answer_1:
    print('Ответ верный!Вы получаете 10 баллов!')
    count += 10
    right_answer += 1
else:
    print(f'Неправильно.Правильный ответ: {answer_1}')


user_input = input(question_2)
if user_input == answer_2:
    print('Ответ верный!Вы получаете 10 баллов!')
    count += 10
    right_answer += 1
else:
    print(f'Неправильно.Правильный ответ: {answer_2}')

user_input = input(question_3)
if user_input == answer_3:
    print('Ответ верный!Вы получаете 10 баллов!')
    count += 10
    right_answer += 1
else:
    print(f'Неправильно.Правильный ответ: {answer_3}')

procent_answer = round(right_answer / 3 * 100, 1)
print('....')
print(f'''Вот и всё, {user_name}!
Вы ответили на {right_answer} вопросов из 3 верно.
Вы заработали {count} баллов.
Это {procent_answer} процентов.
''')

