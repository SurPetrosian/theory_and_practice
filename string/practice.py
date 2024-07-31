# Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет, имеется ли подстрока subst в
# строке st. В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!». Должно быть найдено
# совпадение независимо от регистра обеих строк.

# def search_substr(subst, st):
#     if subst in st:
#         print("Есть контакт!")
#     else:
#         print("Мимо!")
#
#
# search_substr("on", "Jon")

#  Напишите программу на Python для подсчета количества символов (частоты символов) в строке. Перейти к редактору
# Пример строки: google.com'
# Ожидаемый результат: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


# str_1 = "google.com"
# dict = {}
# for n in str_1:
#     keys = dict.keys()
#     if n in keys:
#         dict[n] += 1
#     else:
#         dict[n] = 1
# print(dict)
#


# Напишите программу на Python, чтобы получить строку из первых 2 и последних 2 символов из заданной строки. Если
# длина строки меньше 2, верните вместо пустой строки


# def first_and_last(word_1):
#     empty_str = ''
#     if len(word_1) <= 4:
#         return word_1[0:2]
#     elif len(word_1) > 4:
#         return word_1[0:2] + word_1[-2:]
#     elif len(word_1) < 2:
#         return empty_str
#
#
# print(first_and_last("suren"))


# Напишите программу на Python, чтобы получить строку из заданной строки, в которой все вхождения ее первого символа
# были заменены на '$', кроме самого первого символа.


# def change_char(str1):
#   char = str1[0]
#   str1 = str1.replace(char, '$')
#   str1 = char + str1[1:]
#   return str1
# print(change_char('restart'))


# Напишите программу на Python, чтобы получить одну строку из двух заданных строк, разделенных пробелом, и поменять
# местами первые два символа каждой строки.


# def change_place_word(str_1, str_2):
#     char_1 = str_1[1:]
#     char_2 = str_2[1:]
#     return str_1.replace(char_1, char_2) + " " + str_2.replace(char_2, char_1)    # это я так решил
#
#
# print(change_place_word("sur", "pet"))


# def chars_mix_up(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]                         # это решение на сайте
#   return new_a + ' ' + new_b
# print(chars_mix_up('abc', 'xyz'))


# Напишите программу на Python для добавления 'ing' в конец заданной строки (длина должна быть не менее 3). Если
# данная строка уже заканчивается на «ing», вместо этого добавьте «ly». Если длина строки данной строки меньше 3,
# оставьте ее без изменений.


# def append_word(str_1):
#     if len(str_1) >= 3:
#         if 'ing' not in str_1:
#             str_2 = str_1 + 'ing'         # как я решил
#         else:
#             str_2 = str_1 + 'ly'
#     elif len(str_1) < 3:
#         return "sorry"
#     return str_2
#
#
# print(append_word("lews"))

# def add_string(str1):
#   length = len(str1)
#   if length > 2:
#     if str1[-3:] =='ing':
#       str1 +='ly'
#     else:
#       str1 +='ing'                               # как на сайте
#   return str1
# print(add_string('ab'))
# print(add_string('abc'))
# print(add_string('string'))


#  Напишите функцию Python, которая берет список слов и возвращает длину самого длинного.

# def the_longest_word(str_1):
#     longest_word = []
#     for i in str_1:
#         if len(i) > len(longest_word):
#             longest_word = i
#     return len(longest_word)
#
#
# print(the_longest_word(['ssssqqq', 'dddddd', 'd']))


# Напишите программу на Python для удаления n- го символа индекса из непустой строки.

# def delete_letter(str_1, integer_1):
#     str_2 = []
#     for i in str_1:
#         str_2.append(i)
#     del str_2[integer_1]                          # я решил так
#     return ''.join(str_2)
#
#
# print(delete_letter("angel", 1))

# def remove_char(str, n):
#     first_part = str[:n]                         # можно было решить срезами
#     last_part = str[n + 1:]
#     return first_part + last_part


# # Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# s = input()
# for i in s:
#     if s.count(i) == 1:
#         print(s.find(i))
#         break
#     elif s.count(i) > 1:
#         print(-1)
#         break


