# Словари — изменяемый тип Ключ — имя для доступа к ячейке с данными. Ключом в словаре могут быть любые
# **неизменяемые типы данных**, например: строки, числа, булев тип и т. д. Список и другой словарь ключами быть не
# могут. Два элемента не могут иметь одинаковый ключ. Значение** — всё, что мы положили в ячейку с определенным
# ключом. Значением ключа в словаре может быть любой тип данных: строки, числа, булево значение, списки.

# создание словаря с помощью dict
n = dict(name=1, age=26, country=2)  # ключи обязательно должны быть строками
print(n)

# создание словаря с помощью dict.fromkeys()

new_dictionary = dict.fromkeys(['a', 'b', 'c'], 11)  # в этом случае создается словарь с ключами из списка и со
# значениями 11 для всех, если не указать значение, то будет автоматом none
print(new_dictionary)

dictionary_1 = {1: 'apple',
                2: 'banana'}
print(dictionary_1[1])

dictionary_1[1] = 'cherry'  # так мы изменяем значение
print(dictionary_1)

# Переменную можно использовать в качестве ключа:
number = 1
dictionary_1[number] = 'apple'
print(dictionary_1)

# Из словаря можно удалять элементы по ключу
del dictionary_1[2]
print(dictionary_1)

# В словарь можно добавить также по ключу
dictionary_1 = {1: 'apple', 2: 'banana'}

dictionary_1[3] = 'cherry'
print(dictionary_1)
# Методы Keys и Values

dictionary_2 = {'name': "David", 'age': 23, 'country': "Australia"}
print(dictionary_2.keys())  # выводит все ключи как список
print(dictionary_2.values())  # выводит все значения как список


# Чтобы вывести все ключи, просто используйте перебор словаря:

dictionary_3 = {'name': "David", 'age': 23, 'country': "Australia"}

for key in dictionary_3:
    print(key)

# С помощью ключей можно получить доступ и к значениям:
dictionary_3 = {'name': "David", 'age': 23, 'country': "Australia"}

for key in dictionary_3:
    print(dictionary_3[key])

# длина словаря
dictionary_3 = {'name': "David", 'age': 23, 'country': "Australia"}
print(len(dictionary_3))
