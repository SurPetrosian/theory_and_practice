import random

user_input = input('Введите ваше имя: ')
count = 0


def random_words():
    with open("word.txt", "r") as file:
        global count
        for word in file:
            select_word = word.replace("\n", "")
            random_word = random.sample(select_word, len(select_word))
            # random_word.remove("\n")
            user_ = input(f"угадайте слово: {''.join(random_word)}")
            if user_ == select_word:
                print('Верно! Вы получаете 10 очков.')
                count += 10
            else:
                print(f"Неверно! Верный ответ – {select_word}")

    with open("history.txt", 'a') as file:
        file.write(user_input + ' ' + str(count) + '\n')

    with open("history.txt", 'r') as file:
        score_list = []
        for line in file.readlines():
            points = line.split(' ')[1]
            score_list.append(int(points))
        print(f"Количество игр: {len(score_list)}\nРекорд: {max(score_list)}")


random_words()









# import random
#
#
# def load_file():
#     with open('word.txt', 'r', encoding='utf-8') as file:
#         data = file.read().splitlines()
#
#         return data
#
#
# def mix_word(word):
#     list_ = list(word)
#     random.shuffle(list_)
#     return " ".join(list_)
#
#
# def read_top():
#     score_list = []
#     with open('history.txt', 'r', encoding='utf-8') as file:
#         for line in file.readlines():
#             points = line.split(' ')[1]
#             score_list.append(int(points))
#
#     return f"Количество игр: {len(score_list)}\nРекорд: {max(score_list)}"
#
#
# def save_game(name, score):
#     with open('history.txt', 'a', encoding='utf-8') as file:
#         file.write(f'\n{name} {score}')
#
#
# def main():
#     user_name = input("Введите ваше имя: ")
#     word_list = load_file()
#
#     score = 0
#     for word in word_list:
#         shuffle_word = mix_word(word)
#         user_answer = input(f"Угадайте слово: {shuffle_word}\n").lower()
#         if user_answer == word:
#             print('Верно вы получаете 10 очков')
#             score += 10
#         else:
#             print(f"Неверно! Верный ответ - {word}")
#     print(f"Игра окончена! Ты набрал {score} очков")
#     save_game(user_name, score)
#
#     print(read_top())
#
#
# main()
