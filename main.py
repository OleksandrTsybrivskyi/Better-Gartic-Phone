import telebot

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    telegram_id = message.from_user.id
    bot.send_message(telegram_id, "Привіт")


bot.polling(none_stop=True)