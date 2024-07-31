words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {}

level = input(
    'Выберите уровень сложности.\n'
    'Легкий, средний, сложный.'
)

if level == 'легкий':
    words = words_easy
elif level == 'средний':
    words = words_medium
elif level == 'сложный':
    words = words_hard

user_level = 0

for key, values in words.items():
    print(key, len(values), 'букв', 'начинается на', values[0])
    user_input = input()
    if user_input == values:
        print(f'Верно {key} это {values}')
        answers[key] = True
        user_level += 1
    else:
        print(f'Неверно {key} это {values}')
        answers[key] = False

right_answer = []
no_right = []

for key, values in answers.items():
    if values:
        right_answer.append(key)
    else:
        no_right.append(key)

a = '\n'.join(right_answer)
b = '\n'.join(no_right)

print(f"Правильно отвечены слова: \n{a}")
print(f"Не правильно отвечены слова: \n{b}")

if user_level in levels:
    print(f'Ваш ранг: {levels[user_level]}')
