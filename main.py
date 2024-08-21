import telebot

bot = telebot.TeleBot('5735611297:AAFE57qTOthE68bUCz5JewVAcFr3hN1DlT0')


@bot.message_handler(commands=['start'])
def start(message):
    telegram_id = message.from_user.id
    bot.send_message(telegram_id, "Привіт")


bot.polling(none_stop=True)