from telebot import TeleBot
#imports keyboard
from telebot import types

TOKEN = 'PLACE TOKEN HERE'
bot = TeleBot(TOKEN)
#allows you to specify a URL for automatically sending updates to the bot via an outgoing webhook
bot.set_webhook()

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'YOUR MESSAGE GOES HERE')

    #trial versions keyboard buttons(1,2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Button 1')
    btn2 = types.KeyboardButton(text='Button 2')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, 'YOUR MESSAGE GOES HERE', reply_markup=keyboard)


bot.infinity_polling()