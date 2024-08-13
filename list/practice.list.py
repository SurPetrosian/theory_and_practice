# # 1. Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует, замените его на 200.
# # Обновите список только при первом вхождении числа 20.
#
# number = [1, 3, 4, 11, 20, 20]
# a = number.index(20)
# number[a] = 200
# print(number)
#
# # 2. Необходимо удалить пустые строки из списка строк.
#
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# resList = list(filter(None, list1))  # можно с помощью функцию фильтр
# print(resList)
#
# # 3. Дан список чисел. Превратите его в список квадратов этих чисел.
#
# number_1 = [1, 4, 6, 9]
# number_2 = []
# for num in number_1:
#     num = num * num
#     number_2.append(num)
# print(number_2)
#
# aList = [1, 2, 3, 4, 5, 6, 7]
# aList = [x * x for x in aList]  # можно решить таким образом
# print(aList)
#
# # 3. Необходимо вывести список в обратном порядке.
#
# b_list = [2, 'dsdsd', 3]
# b_list.reverse()
# print(b_list)  # я так решил
#
# aList = [100, 200, 300, 400, 500]
# aList = aList[::-1]  # можно решить так
# print(aList)
#
#
# # Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. В исходном
# # списке минимум 2 элемента.
# def change(lst):
#
#     return lst
#
#
# print(change([0, 2, 6, 8]))


# def dig_pow(n, p):
#     a = 0
#     for i in range(len(str(n))):               #num = str(n)
#                                                # total = sum([int(num[i]) ** (p + i) for i in range(len(num))])
#                                                # return total / n if (total % n) == 0 else -1
#         s = (int(str(n)[i])) ** p
#         p += 1
#         a += s
#     k = a / n
#
#     if a < n:
#         return -1
#     else:
#         return int(k)



