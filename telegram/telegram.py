import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("7487286391:AAH53adlB149559HCzBN5zW0sJKMzdGFkXg")


@bot.message_handler(commands=['site', 'сайт', 'веб-сайт', 'web-site'])
def site(message):
    webbrowser.open('https://www.wildberries.ru/brands/311112394-rich-and-kind-beauty')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Чем могу помочь?')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Вот ваш ID: {message.from_user.id}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://www.wildberries.ru/brands/311112394-rich-and-kind-beauty'))
    bot.reply_to(message, 'фото отправлены менеджеру', reply_markup=markup)


bot.polling(none_stop=True)
