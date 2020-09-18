import telebot

bot = telebot.TeleBot('1392723978:AAFnckkjU61gWjePx3e2gu9ZkXcczSTQdpg')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет,ты написал мне /start', reply_markup=keyboard)


@bot.message_handler(content_types=['text', 'video'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет!Как твои дела?')
    elif message.text.lower() == 'хорошо':
        bot.send_message(message.chat.id, 'Жыве Беларусь?')
    elif message.text.lower() == 'жыве':
        bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAIFyl9GJ87YuS5dp6eouEOPWdNsOtNtAAI7AgACCbj8BeaeQzzSW2OlGwQ')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай друг')
    elif message.text.lower() == 'ублюдок':
        bot.send_document(message.chat.id, 'https://static.life.ru/publications/2020/7/6/665237996492.8094.gif')


keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Привет', 'Пока', 'Хорошо', 'Жыве', 'Ублюдок')
bot.polling()
