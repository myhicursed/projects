import telebot
from telebot import types

bot = telebot.TeleBot('7755694735:AAFuwcul-QlD8D8B1N44AeB0V7ybh1NAdjI')
user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Авторизация")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Авторизуйтесь", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Авторизация':
        msg = bot.send_message(message.from_user.id, '❓ Логин')
        bot.register_next_step_handler(msg, get_password)

def get_password(message):
    login = message.text
    msg = bot.send_message(message.chat.id, f'Логин: {login}\n❓ Введите пароль')
    bot.register_next_step_handler(msg, check_auth, login)

def check_auth(message, login):
    password = message.text
    if login == 'admin' and password == '123':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Показать график работы📊')
        btn2 = types.KeyboardButton('Начать смену🚍')
        btn3 = types.KeyboardButton('Завершить смену🙅')
        btn4 = types.KeyboardButton('Сообщить о поломке💁‍♀️')
        btn5 = types.KeyboardButton('Сообщить о ДТП💀')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, '✅ Авторизация успешна!', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, '❌ Неверный логин или пароль')










bot.polling(none_stop=True, interval=0)