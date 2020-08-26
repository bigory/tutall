import telebot

bot = telebot.TeleBot('1392723978:AAFnckkjU61gWjePx3e2gu9ZkXcczSTQdpg')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет,ты написал старт')


bot.polling()
