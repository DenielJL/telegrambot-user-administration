from telebot import TeleBot
from telebot import types

TOKEN = 'PLACE TOKEN HERE'
bot = TeleBot(TOKEN)

GROUP_CHAT_ID = TELEGRAM GROUP ID PLACE HERE

user_states = {}


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'YOUR MESSAGE GOES HERE')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_info = types.KeyboardButton(text='YOUR MESSAGE GOES HERE')
    btn_signup = types.KeyboardButton(text='Хочу записаться на курсы')
    btn_mail = types.KeyboardButton(text='YOUR MESSAGE GOES HERE')
    btn_talk = types.KeyboardButton(text='YOUR MESSAGE GOES HERE')
    keyboard.add(btn_info, btn_signup, btn_mail, btn_talk)
    bot.send_message(message.chat.id, 'YOUR MESSAGE GOES HERE', reply_markup=keyboard)

    user_states[message.chat.id] = 'normal'


@bot.message_handler(func=lambda message: message.text == 'BOT MESSAGE GOES HERE')
def handle_button1(message):
    bot.send_message(message.chat.id, 'BOT ANSWER GOES HERE')
    user_states[message.chat.id] = 'normal'


@bot.message_handler(func=lambda message: message.text == 'BOT MESSAGE GOES HERE')
def handle_button2(message):
    bot.send_message(message.chat.id, 'BOT ANSWER GOES HERE')
    user_states[message.chat.id] = 'normal'


@bot.message_handler(func=lambda message: message.text == 'BOT MESSAGE GOES HERE')
def handle_button3(message):
    bot.send_message(message.chat.id, 'BOT ANSWER GOES HERE')
    user_states[message.chat.id] = 'normal'


@bot.message_handler(func=lambda message: message.text == 'BOT MESSAGE GOES HERE')
def handle_talk_button(message):
    bot.send_message(message.chat.id,'BOT ANSWER GOES HERE')

    talk_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_stop = types.KeyboardButton(text='EXIT TALK')
    talk_keyboard.add(btn_stop)
    bot.send_message(message.chat.id, 'Нажмите "BUTTON FOR EXIT TALK',
                     reply_markup=talk_keyboard)

    user_states[message.chat.id] = 'talking'


@bot.message_handler(func=lambda message: message.text == 'EXIT TALK')
def handle_stop_talking(message):
    if user_states.get(message.chat.id) == 'talking':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_info = types.KeyboardButton(text='YOUR MESSAGE GOES HERE')
        btn_signup = types.KeyboardButton(text='YOUR MESSAGE GOES HERE')
        btn_mail = types.KeyboardButton(text='YOUR MESSAGE GOES HERE')
        btn_talk = types.KeyboardButton(text='YOUR MESSAGE GOES HERE')
        keyboard.add(btn_info, btn_signup, btn_mail, btn_talk)

        bot.send_message(message.chat.id, 'YOU EXIT TALK:', reply_markup=keyboard)
        user_states[message.chat.id] = 'normal'

        stop_text = f"USER @{message.from_user.username or 'без username'} (ID: {message.from_user.id}) EXIT TALK."
        bot.send_message(GROUP_CHAT_ID, stop_text)


@bot.message_handler(func=lambda message: user_states.get(
    message.chat.id) == 'talking' and message.text != 'YOUR MESSAGE GOES HERE' and message.text != 'EXIT TALK')
def handle_user_message(message):
    forward_text = f"YOUR MESSAGE GOES HERE @{message.from_user.username or 'без username'} (ID: {message.from_user.id}):\n\n{message.text}"
    bot.send_message(GROUP_CHAT_ID, forward_text)
    bot.send_message(message.chat.id, 'MESSAGE SEND TO ADMIN!')


@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    if user_states.get(message.chat.id) == 'talking':
        handle_user_message(message)
    else:
        bot.send_message(message.chat.id, 'CHOOSE BUTTON!')


bot.infinity_polling()