#  Строки записываются с помощью одинарных или двойных кавычек
print("hello world")
print('hello world')

# В строке мы можем обращаться к конкретным буквам по их индексу и срезам:

s = 'Suren Petrosian'
print(s[0])
print(s[6])
print(s[1:9])


# Можем подсчитать длину строки
print(len(s))

# Строка — это итерируемый объект, и ее можно перебрать циклом for.
name = 'APPLE'
a = []
for i in name:
    a.append(i)
print(a)


