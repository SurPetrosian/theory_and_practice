import telebot

bot = telebot.TeleBot("7487286391:AAH53adlB149559HCzBN5zW0sJKMzdGFkXg")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'барев, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'бана эхе апэ')


bot.polling(none_stop=True)
