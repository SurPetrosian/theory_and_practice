# Функция — объект (типа function), который объединяет несколько инструкций в одном блоке для последующего
# использования. Аргументы — всё, что передается в функцию. Например, в print(message) message — это аргумент
# функции.
# Позиционные аргументы — это обычные аргументы, которые передаются по порядку. Например, при вызове round(
# 1.333, 2) 1.333 — это первый аргумент функции, а 2 — второй.

# как создается функция
def say_something():
    print('something')


say_something()  # вот так вызывается функция, 2 отступа от самой функции


# return позволяет нам получить результат работы функции и использовать его дальше в нашей программе.
def get_alphabet():
    alphabet = "abcdefgh"


letters = get_alphabet()
print(letters)  # выведет None


def get_alphabet():
    alphabet = "abcdefgh"
    return alphabet


letters = get_alphabet()
print(letters)  # выведет abcdefgh


# После выполнения команды return выполнение следующего за ней кода не происходит.


def say_my_name(str_1):
    return str_1 * 3
    print('omg, this is your name')  # вот этот принт не выведет


print(say_my_name('Suren'))


# Одна функция может содержать несколько return.


def is_seven(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_seven(4))


def is_seven(num):
    if num % 2 == 0:
        return True  # Поскольку мы переходим к else, только если число нечетное, можно не использовать этот
    return False  # оператор, а написать так


# Аргументы и функции

def double_int(number):
    a = number * 2  # number - это аргумент
    return a


print(double_int(123))


def double_int_1(number):
    c = number * 2
    return c


b = 123  # в этих случаях мы передаем значение переменной в функцию, а аргумент number это временный аргум
d = 56678934  # а аргумент number это временный аргумент

print(double_int_1(b))
print(double_int_1(d))


def sum_num_2(number, tip=10):  # в этом случаи tip это опциональный аргумент
    h = number * tip
    return h


print(sum_num_2(78))  # мы можем не задавать второй аргумент и тогда будет работать наш опциональный аргумент tip
print(sum_num_2(78, 5))  # в этом случае мы изменяем наш опциональный аргумент на 5

# Как передать любое количество аргументов? Что такое *args?


def new_sum(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


print(new_sum(2, 4, 6, 9))


def multiplication(x):
    print(f'квадрат числа {x} = {x**2}')


for i in range(1, 33):
    multiplication(i)




