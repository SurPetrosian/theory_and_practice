# Для получения значения ключи пишутся последовательно в квадратных скобках.
# store = {
#     "apples": {"name":"Яблоки", "price":"100", "available": 40},
#     "oranges": {"name":"Апельсины", "price":"200", "available": 20},
#     "pomegranate": {"name":"Гранаты", "price":"400", "available": 5},
# }
#
# print(store["apples"]["name"])
# print(store["oranges"]["available"])
#
# # Если мы хотим использовать цикл, можно использовать items():
# store = {
#     "apples": {"name":"Яблоки", "price":"100", "available": 40},
#     "oranges": {"name":"Апельсины", "price":"200", "available": 20},
#     "pomegranate": {"name":"Гранаты", "price":"400", "available": 5},
# }
#
# for item in store.values():
#     print(item["name"], item["price"])

# А можно использовать ключи:
store = {
    "apples": {"name":"Яблоки", "price":"100", "available": 40},
    "oranges": {"name":"Апельсины", "price":"200", "available": 20},
    "pomegranate": {"name":"Гранаты", "price":"400", "available": 5},
}

for key in store:
    print(store[key]["name"], store[key]["price"])