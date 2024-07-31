# Set — это набор или множество. Первое, что нужно знать, — в нем не может быть повторяющихся элементов. Множества не
# упорядочены, поэтому индексов и слайсов у них нет.
# в set используется фигурные скобки

my_languages = {'Armenian', 'Russian', 'English'}

# Уникализация списка через множество:
b = ['python', 'java', 'javascript', 'java', 'python']
c = set(b)
print(c)  # в результате из списка уберутся повторяющейся элементы

# add — добавляет элемент в множество.
# discard — удаляет элемент, если он находится в множестве.
# remove — тоже удаляет элемент из множества. KeyError, если такого элемента не существует.

my_car = {'reno', 'lada'}
my_car.add('hundai')
print(my_car)

my_car.discard('reno')
print(my_car)

# можем запустить итерацию

my_future_car = {'ferrari', 'audi', 'bmw'}

for i in my_future_car:
    print(i)

# union — соединяет множества
my_favorite_car = {'ferrari', 'audi', 'bmw', 'reno'}
my_car = {'reno', 'lada'}

print(my_car.union(my_favorite_car))

# intersection — это пересечение
my_favorite_car = {'ferrari', 'audi', 'bmw', 'reno'}
my_car = {'reno', 'lada', 'audi'}


print(my_car.intersection(my_favorite_car))  # выдаст рено и ауди, то есть машины которые у меня уже
# есть из списка favorite

# difference — это вычитание
my_favorite_car = {'ferrari', 'audi', 'bmw', 'reno'}
my_car = {'reno', 'lada', 'audi'}

print(my_car.difference(my_favorite_car))  # выдаст лада, это машина не входит в мой favorite

# issubset — возвращает булев тип,
# сообщает, имею ли я все машины из списка favorite

print(my_car.issubset(my_favorite_car))