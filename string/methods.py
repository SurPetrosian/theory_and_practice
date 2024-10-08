# .upper() превращает все буквы заглавную
p = 'hello'
s = p.upper()
print(s)

# .lower() превращает все буквы в маленькие
d = 'HELLO'
f = p.lower()
print(f)

# .split() разбивает нашу строку по пробелам и собирает в список
m = 'ivanov ivan ivanovich'
print(m.split())

# .join() используется для превращения списка со строками обратно в строку, в кавычках нужно указать символ который
# будет между строками
names = ['Bob', 'Jack', 'Sam']
names_str = ', '.join(names)
print(names_str)


# .count() проверяет сколько раз этот аргумент есть в строке
k = "good"
print(k.count('o'))

# .find() ищет индекс подстроки, если подстрок много, то вернет первый слева
name = 'Suren'
print(name.find('S'))

# .rfind() ищет индекс подстроки справа

# .index() также ищет индекс, но если нет подстроки выдает ошибку а find выдает -1

# .replace() меняет подстроку на ту, которую указали, также можем убрать букву указав второй аргумент пробел
surname = "Petrosian"
sur = surname.replace("t", 'd')
print(sur)

# .isalpha() проверяет состоять ли строка только из букв

name_1 = "Suren"

if name_1.isalpha():
    print("строка состоит только из букв")

# .isdigit() проверяет, состоит ли строка только из цифр
