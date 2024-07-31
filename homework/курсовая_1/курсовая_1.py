import random

list_morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

english_words = ["code", "bit", "soul", "next"]
answers = []


def morse_encode(word):
    list_1 = []
    for w in word:
        list_1.append(w)
    list_2 = []
    for i in list_1:
        if i in list_morse:
            list_2.append(list_morse[i])
    return ' '.join(list_2)


def get_word(word):
    random_word = random.choice(word)
    # return ''.join(random_word)
    return random_word


# a = morse_encode('code')
# print(a)

print("""Сегодня мы потренируемся расшифровывать азбуку Морзе
Нажмите Enter и начнем""")

for i in range(5):
    # for word in english_words:
    word_1 = get_word(english_words)
    print(word_1)
    word_2 = morse_encode(word_1)
    user_input = input()
    if user_input == word_2:
        print(f'Верно это слово {word_1}')
        answers.append(True)
    else:
        print('неверно')
        answers.append(False)

print(f"Всего задачек: {len(answers)}\nОтвечено верно:{answers.count(True)}\nОтвечено неверно: {answers.count(False)}")
