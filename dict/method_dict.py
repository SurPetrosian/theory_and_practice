# метод clear() очищает словарь
new_dict = {1: "one", 2: "two"}
new_dict.clear()
print(new_dict)

# метод get() ищет значение по ключу
new_dict_1 = {1: "one", 2: "two"}
print(new_dict_1.get(1))
print(new_dict_1.get(3))  # выдаст none
print(new_dict_1.get(4, 'нет такого ключа'))  # в этом случае также нет значения, но выдаст следующий аргумент который
# указали

# метод setdefault() ищет значение по ключу и если нет то создает
new_dict_1 = {1: "one", 2: "two"}
print(new_dict_1.setdefault(3))
print(new_dict_1)  # создает по ключу 3 значение None
print(new_dict_1.setdefault(4, 'four'))  # создает по ключу 4 значение 'four'
print(new_dict_1)

# метод pop() удаляет по ключу значение и выводит, в скобках нужно обязательно указывать ключ
new_dict_2 = {1: 'one', 2: 'two', 3: None, 4: 'four'}
print(new_dict_2.pop(3))
print(new_dict_2)

# метод popitem() удаляет хаотично ключ и значение и выводит
new_dict_3 = {1: 'one', 2: 'two', 3: None, 4: 'four', 5: 'five'}
print(new_dict_3.popitem())  # тут не нужно указывать ключ

# Методы Keys и Values

dictionary_2 = {'name': "David", 'age': 23, 'country': "Australia"}
print(dictionary_2.keys())  # выводит все ключи как список
print(dictionary_2.values())  # выводит все значения как список

# Чтобы вывести содержимое словаря в формате ключ - значение, используйте items:
dictionary_3 = {'name': "David", 'age': 23, 'country': "Australia"}

for key, item in dictionary_3.items():
    print(key, item)

