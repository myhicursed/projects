import telebot
import psycopg2

TOKEN = "7755694735:AAFuwcul-QlD8D8B1N44AeB0V7ybh1NAdjI"
bot = telebot.TeleBot(TOKEN)


user_data = {}

@bot.message_handler(commands=['table'])
def send_table(message):
    chat_id = message.chat.id
    if chat_id in user_data and user_data.get(chat_id, {}).get("authenticated"):
        bot.reply_to(message, "📊 Вот ваша таблица:\n"
                              "| ID | Имя  | Возраст |\n"
                              "|----|------|---------|\n"
                              "| 1  | Иван | 25      |\n"
                              "| 2  | Анна | 30      |")
    else:
        bot.reply_to(message, "❌ Доступ запрещен. Сначала авторизуйтесь через /start!")

@bot.message_handler(commands=['start'])
def ask_login(message):
    chat_id = message.chat.id
    user_data[chat_id] = {"step": "waiting_login"}
    bot.send_message(chat_id, "🔑 Введите логин:")


@bot.message_handler(func=lambda message: True)
def handle_auth(message):
    chat_id = message.chat.id

    if chat_id not in user_data:
        bot.send_message(chat_id, "Напишите /start для авторизации.")
        return

    if user_data[chat_id]["step"] == "waiting_login":
        user_data[chat_id]["login"] = message.text
        user_data[chat_id]["step"] = "waiting_password"
        bot.send_message(chat_id, "🔒 Введите пароль:")

    elif user_data[chat_id]["step"] == "waiting_password":
        user_data[chat_id]["password"] = message.text
        login = user_data[chat_id]["login"]
        password = user_data[chat_id]["password"]
        try:
            conn = psycopg2.connect(
                host = 'localhost',
                database = 'buspark',
                user = 'postgres',
                password = 'myhicursed',
                port = '5432'
            )
        except:
            print('Не удалось установить соединение')

        cursor = conn.cursor()
        cursor.execute(""" SELECT user_password 
                                                      FROM users
                                                      WHERE user_login = %s;
        """, (login,))
        record_password = cursor.fetchall()
        if not record_password:
            return bot.reply_to(message, 'Неверный пароль')
        else:
            current_password = record_password[0]
            if password == current_password[0]:
                print('Авторизация пройдена')
                bot.send_message(chat_id, "✅ Успешный вход! Доступ разрешен.")
                cursor.close()
                print(f'login: {login}')
                user_data[chat_id]["authenticated"] = True
            else:
                print('Неверный логин/пароль')
                bot.send_message(chat_id, "❌ Неверный логин или пароль!")





bot.polling()