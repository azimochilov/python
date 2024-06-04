import telebot
from transliterate import to_latin, to_cyrillic
bot = telebot.TeleBot("7247467432:AAHrZsy2QLnjeyEJbkPlMb657fztHz-rGA0", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Salam aleykum, Welcome home ? , koro do'ngmi?")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	msg = message.text
	if msg.isascii():
		answ = to_cyrillic(msg)
	else:
		answ = to_latin(msg)
	bot.reply_to(message, answ)

bot.infinity_polling()