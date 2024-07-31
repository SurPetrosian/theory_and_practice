# questions = ['My name ___ Vova.', 'I ___ a coder', 'I live ___ Moscow.']
# answers = ['is', 'am', 'in']
#
# user_ = input(
#     '''Привет!
# Предлагаю проверить свои знания английского!
# Наберите "ready", чтобы начать!
#     '''
# )
# right_answer = 0
# count = 0
# if user_ == "ready":
#     for i in range(len(questions)):
#         question = questions[i]
#         answer = answers[i]
#         user_input = input(question)
#         for g in range(len(answers)):
#             if user_input == answer:
#                 print("Ответ верный!")
#                 count += 10
#                 right_answer += 1
#                 break
#             else:
#                 print('no')
#
#
#     procent_answer = round(right_answer / 3 * 100, 1)
#     print('....')
#     print(f'''Вот и всё, Вы ответили на {right_answer} вопросов из 3 верно.
# Вы заработали {count} баллов.
# Это {procent_answer} процентов.
#     ''')
# else:
#     print("Кажется, вы не хотите играть. Очень жаль.")


questions = ['My name ___  Vova ', 'I ___ a coder ', 'I live ___ Moscow ', ]
answers = ['is', 'am', 'in', ]

user_score = 0  # кол-во заработнанных очков
answered_questions = 0  # кол-во верных ответов
total_questions = len(questions)

print(
    "Привет! Предлагаю проверить свои знания английского! "
    "Набери 'ready', чтобы начать! "
)
user_input = input('')

if user_input != 'ready':
    print("Кажется, вы не хотите играть. Очень жаль.")
else:
    for question_index in range(total_questions):
        question = questions[question_index]
        answer = answers[question_index]
        print(question)

        for attempts_left in range(3, 0, -1):
            user_answer = input()
            if user_answer == answer:
                print('Ответ верный!')
                user_score += attempts_left
                answered_questions += 1
                break
            elif attempts_left == 1:
                print(f'Неправильно. Правильный ответ: {answers[question_index]}')
            else:
                print(f'Осталось попыток: {attempts_left-1}, попробуйте еще раз!')

    right_percentage = round((user_score / total_questions) * 100, 2)

    print(
        f'Вот и все! '
        f'Вы ответили на {answered_questions} вопросов из {total_questions} верно '
        f'и заработали {user_score} очков'
    )