from telebot import TeleBot

TOKEN = 'PLACE TOKEN HERE'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello world!')

bot.infinity_polling()