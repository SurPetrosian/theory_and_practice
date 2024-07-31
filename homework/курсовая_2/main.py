from clas import Player
from utils import load_random_word


username = input('Введите имя игрока: ')
player = Player(username)
word = load_random_word()


print(f'Привет, {player}')
print(f'Составьте {word.subwords_count()} слов из слова {word}')
print('Слова должны быть не короче 3 букв')
print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
print('Поехали, ваше первое слово? \n')


while player.usedwords_count() != word.subwords_count():
    user_input = input()
    if user_input == "stop":
        break
    if len(user_input) < 3:
        print('Слишком короткое слово')
        continue
    if word.check_word(user_input):
        if not player.check_used(user_input):
            print('верно')
            player.add_word(user_input)
        else:
            print('уже исползовано')
    else:
        print('неверно')
print(f'Игра завершена, вы угадали {player.usedwords_count()} слов!')