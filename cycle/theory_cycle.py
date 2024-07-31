# Цикл — это управляющая конструкция для многократного исполнения инструкций.
# В Python цикл состоит из оператора for или while, условия и тела цикла.


# Задачи, которые можно решить с помощью цикла for

# Вывести все элементы списка:
# letters = ['s', 'u', 'r', 'e', 'n']
# for num in letters:
#     print(num)

# Пронумеровать элементы списка:
# letters_1 = ['s', 'u', 'r', 'e', 'n']
# num_1 = 0
# for i in letters_1:
#     print(f'{num_1} = {i}')
#     num_1 += 1

# Просуммировать все элементы списка:
# num_sum = 0
# number_1 = [100, 300, 430032234]
# for i in number_1:
#     num_sum += i
# print(num_sum)

# Вывести часть элементов списка:

# words = ['a', 'b', 'c', 'd']
# for i in words:
#     if i == 'a':
#         print(i)

# Задачи, которые можно решить с помощью цикла while

# Посчитать от 0 до 9 помощью while:
# i = 0
# while i < 10:
#     print(f"i = {i}")
#     i += 1

# Запустить бесконечный цикл:
# answer = None
# while answer != 'пошли':
#     answer = input('пошли тусить')
# print('я знал что хочешь')

# Конструкция for in range

# for b in range(5):
#     print(b)

# Перебрать список, перебирая индексы:

# list_word = ['use it', 'by it', 'close it', 'open it']
# list_indexes = range(len(list_word))
# for num_indexes in list_indexes:
#     print(list_word[num_indexes])

# Continue используется, как и break, но не прерывает цикл, а завершает текущую итерацию — сразу запускается следующая.

# x = 9
# while x:
#     x -= 1
#     if x % 2 == 0: continue
#     print(x, end=',')

# List comprehensions — это еще один способ работать с итерируемыми объектами, например списками, который позволяет
# перейти от создания списков с помощью циклов к более компактным конструкциям.
# [<что будет в списке> for <временная переменная списка> in <список>]

# a = []
# for item in range(1, 10):
#     a.append(item)
# print(a)

#  можно записать так
# a = [item for item in range(1, 10)]
# print(a)

# pass - такой код называют блоком условия или цикла. Для циклов еще распространено название тело цикла.

for i in range(7):
    pass  # тут будет код, нужно написать его, вперед

letters = ["A", "B", "C", "D", "E", "F"]

# for i in range(len(letters)):
#     print(f'{i} {letters[i]}')

# Функция enumerate (от англ. «Пронумеровать») позволяет перебирать не одну переменную, а сразу несколько,
# где в первую временную переменную попадает индекс (порядковый номер начиная с 0), а во вторую — значение.

for i, letter in enumerate(letters):
    print(i, letter)  # можно верхний код записать в таком формате, используя функцию enumerate

for i, letter in enumerate(letters, start=1):  # чтобы нумерация начался с 1
    print(i, letter)
