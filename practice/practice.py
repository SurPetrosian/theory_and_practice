from datetime import date, time, datetime

# Задача 1
# # Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# # Выведите все элементы, которые меньше 5.
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)
#
# # Задача 2
# # Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
#
# c = []
# for i in a:
#     for h in b:
#         if i not in c:
#             if i == h:
#                 c.append(i)
#
# print(c)
#
# result = list(filter(lambda elem: elem in b, a))  # решения на сайте
# print(result)
#
# # Отсортируйте словарь по значению в порядке возрастания и убывания.
#
# import operator
#
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# result_1 = dict(sorted(d.items(), key=operator.itemgetter(1)))
# result_2 = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
# print(result_1)
# print(result_2)
#
#
# # Простейшие арифметические операции (1) Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
# # третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если — ,
# # то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная
# # операция ".
#
#
# def arithmetic(a, b, c):
#     if c == '+':
#         return a + b
#     elif c == '-':
#         return a - b
#     elif c == '*':
#         return c * b
#     elif c == '/':
#         return c / b
#
#
# print(arithmetic(100, 20, '+'))
#
#
# # Високосный год (2)
# # Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
#
#
# def is_year_leap(year):
#     if year % 4 == 0 and year % 100 != 0:
#         print('год високосный')
#     elif year % 400 == 0:
#         print('год високосный')
#     else:
#         print('год не високосный')
#
#
# is_year_leap(2024)
#
# # Написать функцию square , принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа
# # ): периметр квадрата, площадь квадрата и диагональ квадрата.
#
# import math
#
#
# def square(a):
#     c = a + a + a + a
#     b = a ** 2
#     e = round(math.sqrt(a ** 2 * 2), 2)
#     return c, b, e
#
#
# print(square(19987))
#
#
# def check_pin(pin):
#     if pin.isdigit() == True and len(pin) == 4:
#         return True
#     return False
#
#
# print(check_pin('124'))
#
# estimation = {2: 'Плохо', 3: 'Удовлетворительно', 4: 'Хорошо', 5: 'Отлично'}
#
#
# def get_grade(grade):
#     if grade in estimation:
#         return estimation[grade]
#     return "Ошибка"
#
#
# try:
#     assert get_grade(2) == "Плохо"
#     assert get_grade(3) == "Удовлетворительно"
#     assert get_grade(4) == "Хорошо"
#     assert get_grade(5) == "Отлично"
#     assert get_grade("") == "Ошибка"
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
# else:
#     print("Все хорошо, все работает")
#
# date_one = date(1997, 10, 14)
# print(date_one)
# time_one = time(23, 20, 10)
# print(time_one)
# datetime_one = datetime(1997, 10, 14, 23, 20, 10)
# print(datetime_one)
# print('year', datetime_one.year)
# print(datetime_one.weekday())
# print(datetime.now())
#
# from datetime import date
#
# the_date = date(2027, 10, 5)
#
# print(the_date.year)
# print(the_date.month)
# print(the_date.day)


# # упражнение №1
# print('Petrosian Suren Akobovich')
# print("Mysnikovski rayon Bolshie Sali")
#
# # упражнение №2
# user = input("Введите ваше имя: ")
# print("Добро пожаловать,", user)
#
# # упражнение №3
# len_room = float(input("Введите длину комнаты: "))
# width_room = float(input("Введите ширину комнаты: "))
#
# square_room = len_room * width_room
# print("Площадь комнаты равен:", square_room,"м")

# упражнение №4
# A = 43560
# len_ = int(input("Введите длину сада: "))
# width_ = int(input("Введите ширину сада: "))
#
# square_ = round((len_ * width_ / A), 2)
#
# print("Площадь сада равен:", square_, "акров")
#
# # упражнение №5
# COST_BOTTLE_1 = 0.10
# COST_BOTTLE_2 = 0.25
#
# d_ = int(input("Введите количество бутылок объемом 1л и меньше : "))
# s_ = int(input("Введите количество бутылок объемом больше 1л  : "))
#
# sum_ = round((COST_BOTTLE_1 * d_ + COST_BOTTLE_2 * s_),2)
#
# print("За ваши бутылки вы можете заработать :", sum_, "долларов")

# упражнение №6
# TIPS = 0.18
# TAX = 0.13
# order_amount = int(input("Введите сумму заказа в ресторане:"))
#
# sum_tax = order_amount * TAX
# sum_tips = (order_amount - sum_tax) * TIPS
#
# print("Сумма чаевых - ", sum_tips, " Налог -", sum_tax,"Итог - ", order_amount)

# упражнение №7
# user_number = int(input("Введите число:"))
#
# sum_num = (user_number * (user_number +1)) / 2
# print(sum_num)

# упражнение №8
# A = 0.075
# B = 0.112
#
# sum_a = float(input("Введите количество сувениров - "))
# sum_b = float(input("Введите количество безделушек - "))
#
# total_weight = sum_a * A + sum_b * B
# print("Общий вес равен: ", total_weight)

# упражнение №11
# GALLON = 4.55
# MILES = 1.6
#
# miles = int(input("Введите пройденный путь - "))
# gallon = int(input("Введите количество потраченного топлива - "))
#
#
# km = miles * MILES
# litr = gallon * GALLON
# canada = 100 * litr / km
#
# print("По канадским меркам будет: ", round(canada, 2), "на 100км")

# упражнение №13
# CENTS_PER_TOONIE = 200
# CENTS_PER_LOONIE = 100
# CENTS_PER_QUARTER = 25
# CENTS_PER_DIME =10
# CENTS_PER_NICKEL =5
# # Запрашиваем у пользователя сумму в центах
# cents = int(input("Введите сумму в центах: "))
# # Определим количество двухдолларовых монет путем деления суммы на 200. Затем вычислим # оставшуюся сумму для размена, рассчитав остаток от деления
# print(" ", cents // CENTS_PER_TOONIE, "двухдолларовых монет")
# cents = cents % CENTS_PER_TOONIE
# # Повторяем эти действия для остальных монет
# print(" ", cents // CENTS_PER_LOONIE, "однодолларовых монет")
# cents = cents % CENTS_PER_LOONIE
# print(" ", cents // CENTS_PER_QUARTER, "25–центовых монет")
# cents = cents % CENTS_PER_QUARTER
# print(" ", cents // CENTS_PER_DIME, "10–центовых монет")
# cents = cents % CENTS_PER_DIME
# print(" ", cents // CENTS_PER_NICKEL, "5–центовых монет")
# cents = cents % CENTS_PER_NICKEL
# # Отобразим остаток в центах print(" ", cents, "центов")

# упражнение №18
# PI = 3.14
# radius = float(input("Введите длину  радиуса: "))
# hight = float(input("Введите высоту : "))
#
# volume = round(PI * (radius**2) * hight, 1)
#
# print("Объем цилиндра равен: ", volume)

# упражнение №35
# user_number = int(input("Введите число: "))
# if user_number % 2 == 0:
#     print("Число четное")
# else:
#     print("Число не четное")

# упражнение №36
#
# year_1 = 10.5
# year_2 = 10.5
# other_years = 4
#
# user_age = int(input("Введите возраст: "))
#
# if user_age <= 0:
#     print("Вы ввели не правильно ")

# упражнение №47

# import random
#
# my_name = 'Suren'
# items = random.sample(my_name, 3)
# # result = ''.join(items)
# print(items )
