# # # import random
# # #
# # # with open('word.txt', 'r', encoding="utf-8") as file:
# # #     user_name = input('Введите ваше имя: ')
# # #     points_scored = 0
# # #     for word in file:
# # #         f = random.sample(word, len(word))
# # #         word_1 = ''.join(f)
# # #         result = input(f"Угадайте слово: {word_1}")
# # #         if result in word:
# # #             print("Верно! Вы получаете 10 очков.")
# # #             points_scored += 10
# # #         else:
# # #             print(f"Неверно! Верный ответ – {word}")
# # #     with open('history.txt', 'a') as file:
# # #         file.write('\n' + user_name + ' ')
# # #         file.write(str(points_scored))
# # #     with open('history.txt', 'r') as file:
# # #         games = 0
# # #         records = 0
# # #         for game, record in file:
# # #             games += game
# # #             if record > records:
# # #                 records += record
# # #         print(games)
# # #         print(records)
# # #
# # #
# # #
# # #         # print(f"Всего игр сыграно: {}")
# # #         # print(f"Максимальный рекорд:{}")
# # #
# # # Исходный код
# guides = [ {
#   "pk": 1,
#   "fields": {
#     "user": 2,
#     "surname": "Васечкин",
#     "full_name": "Андрей Васечкин",
#     "tours_count": 5,
#     "bio": "Я обожаю Москву, и изучаю город с необычных ракурсов. С радостью поделюсь с вами своими лучшими открытиями. Мы поднимемся на сталинские высотки и посмотрим на исторический центр сверху. Я покажу вам то, что скрыто от глаз большинства туристов и даже жителей города. Маршруты подобраны индивидуально под ваш запрос. Для влюбленных доступна услуга свидания на крыше.",
#     "is_pro": True,
#     "company": 1
#   }
# },
# {
#   "pk": 2,
#   "fields": {
#     "user": 1,
#     "surname": "Новикова",
#     "full_name": "Людмила Новикова",
#     "tours_count": 2,
#     "bio": "Я петербурженка в 7-м поколении. Люблю делиться историями и секретами дореволюционных петербургских зданий и особняков. Поделюсь историями моей бабушки. Вместе со мной работает небольшая дружная команда влюбленных в Петербург местных гидов. Мы раскроем вам секреты старинных домов и покажем то, что скрыто от глаз большинства туристов и жителей города.",
#     "is_pro": True,
#     "company": 2
#   }
# },
# {
#   "pk": 3,
#   "fields": {
#     "user": 3,
#     "surname": "Беридзе",
#     "full_name": "Георги Беридзе",
#     "tours_count": 5,
#     "bio": "Филолог-журналист по образованию. За плечами более 9 лет экскурсий по Грузии и барменский опыт. Писатель. Перфекционист. И просто увлеченный человек. Родился и вырос в Тбилиси. Более 10 поколений тут. Люблю этот райский уголок на планете и свою работу. Мама-кулинар привила любовь к вкусной еде.",
#     "is_pro": True,
#     "company": None
#   }
# },
# {
#   "pk": 4,
#   "fields": {
#     "user": 4,
#     "surname": "Ласкина",
#     "full_name": "Оксана Ласкина",
#     "tours_count": 2,
#     "bio": "Я всегда увлекалась историей и, как следствие, получила образование гида-экскурсовода. С удовольствием знакомлю гостей города с историей, татарской культурой и традициями. Вы влюбитесь в наш край.",
#     "is_pro": True,
#     "company": 5
#   }
# },
# {
#   "pk": 5,
#   "fields": {
#     "user": 5,
#     "surname": "Горячий",
#     "full_name": "Иван Горячий",
#     "tours_count": 7,
#     "bio": "Работал учителем истории более 10 лет, последние 5 лет живу в Сочи и уже третий год провожу экскурсии, организовываю туры. На моих прогулках и турах вы узнаете не только об экскурсионных объектах, но и о том, чем живет современный Сочи: о ценах, недвижимости, об интересных местах города и его необычных заведениях. Есть туры разного уровня сложности и комфорта, где можно с детьми и без. Бесплатным бонусом ко всем экскурсиям станет фотосессия на зеркальный фотоаппарат.",
#     "is_pro": True,
#     "company": 4
#   }
# },
# {
#   "pk": 6,
#   "fields": {
#     "user": 6,
#     "surname": "Ивлева",
#     "full_name": "Яна Ивлева",
#     "tours_count": 5,
#     "bio": "Я живу в Стамбуле много лет. По образованию филолог и историк. О Стамбуле читаю, пишу, живу этим городом и люблю его. Раскрою его вам таким, какой он есть: великолепный, приветливый, неизменно интересный и всегда загадочный. Ваше путешествие по этому сказочному городу навсегда останется в памяти и сердце. ",
#     "is_pro": True,
#     "company": 1
#   }
# },
# ]
# #
# # for guide in guides:
# #     if guide["fields"]["tours_count"] >= 5:
# #         print(guide["fields"]["full_name"], 'туров:', guide["fields"]["tours_count"] )
#
# user_input = int(input())
# for guide in guides:
#     if user_input == guide["pk"]:
#         print(guide["fields"]["full_name"], 'туров:', guide["fields"]["tours_count"])
#           print(guide["fields"]["bio"])

from datetime import datetime
import requests
import json
import os


API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
CURRENCY_RATES_FILE = 'currency_rates.json'

def main():
    while True:
        currency = input('Введите название валюты (USD или EUR): ')
        if currency not in ("USD", "EUR"):
            print('Некорректный ввод')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f'{currency} к рублю: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('Выберите действие(1 - продолжить, 2 - выйти)')
        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print ('Некорректный ввод')

def get_currency_rate(base: str) -> float:
    """Получает курс от API и возвращает в виде float"""

    url = "https://api.apilayer.com/exchangerates_data/latest"
    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate


def save_to_json(data: dict) -> None:
    """Сохраняет данные в json файл """
    with open(CURRENCY_RATES_FILE, 'a') as f:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], f)
        else:
            with open(CURRENCY_RATES_FILE) as json_file:
                data_list = json.load(json_file)
            data_list.append(data)
            with open(CURRENCY_RATES_FILE, "w") as json_file:
                json.dump(data_list, json_file)


if __name__ == '__main__':
    main()
