import sys
import telebot
from telebot import types
import psycopg2
from design import Ui_MainWindow
from PyQt5.QtCore import QObject, pyqtSignal
import threading





class BusBot(QObject):
    message_signal = pyqtSignal(str, str)
    message_route_name_signal = pyqtSignal(str, str)
    message_end_route_signal = pyqtSignal(str, str)
    message_check_repair_signal = pyqtSignal(str, str)
    def __init__(self):
        super().__init__()
        self.conn = psycopg2.connect(
        host = 'localhost',
        database = 'buspark',
        user = 'postgres',
        password = 'myhicursed',
        port = '5432'
        )

        self.bot = telebot.TeleBot('7755694735:AAFuwcul-QlD8D8B1N44AeB0V7ybh1NAdjI')
        self.user_data = {}

        self.setup_handlers()


    def run(self):
        self.bot.polling(none_stop=True)

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start(message):
            self.start(message)
        
        @self.bot.message_handler(func=lambda message: message.text == '👋 Авторизация')
        def auth_start(message):
            self.handle_auth_start(message)
        
        @self.bot.message_handler(func=lambda message: True)
        def all_messages(message):
            self.handle_message(message)

    def start(self, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Авторизация")
        markup.add(btn1)
        self.bot.send_message(message.from_user.id, "Авторизуйтесь", reply_markup=markup)

    def handle_auth_start(self, message):
        msg = self.bot.send_message(message.from_user.id, '❓ Логин')
        self.bot.register_next_step_handler(msg, self.get_password)
            
    def handle_message(self, message):
        if message.text == 'Сообщить о ДТП💀':
            msg = self.bot.send_message(message.chat.id, "Укажите государственный регистрационный номер автобуса")
            self.bot.register_next_step_handler(msg, self.SendMessageToDispatcher)
        if message.text == 'Показать график📊':
            cursor = self.conn.cursor()
            cursor.execute(" SELECT route_name, bus_number, route_start, route_finally, route_time FROM orders;")
            rows = cursor.fetchall()
            response = 'Ближайшие рейсы: \n'
            for row in rows:
                response += f'Рейс #{row[1]}.\nОтправление из: {row[2]}.\nПрибытие в: {row[3]}\nДата и время в пути: {row[4]} \n'
            self.bot.send_message(message.chat.id, response)
        if message.text == 'Начать смену🚍':
            msg = self.bot.send_message(message.chat.id, "Укажите государственный регистрационный номер автобуса")
            self.bot.register_next_step_handler(msg, self.StartRouteName)
        if message.text == 'Завершить смену🙅':
            msg = self.bot.send_message(message.chat.id, "Укажите номер государственный регистрационный номер автобуса")
            self.bot.register_next_step_handler(msg, self.EndRoute)
        if message.text == 'Сообщить о поломке💁‍♀️':
            msg = self.bot.send_message(message.chat.id, "Укажите номер государственный регистрационный номер автобуса")
            self.bot.register_next_step_handler(msg, self.CheckRepair)
    

    def Accept(self, tg_id, msg):
        print(f'Принят tg_id {tg_id}')
        self.bot.send_message(tg_id, msg)

    def CheckRepair(self, message):
        number = message.text
        curr = str(message.chat.id)
        self.message_check_repair_signal.emit(curr, number)
        self.bot.send_message(message.chat.id, "Информация направлена диспетчеру.")

    def EndRoute(self, message):
        number = message.text
        curr = str(message.chat.id)
        self.message_end_route_signal.emit(curr, number)
        self.bot.send_message(message.chat.id, "Хорошего отдыха!")
    
    #def StartRoute(self, message):
    #    number = message.text
    #    msg = self.bot.send_message(message.chat.id, "Укажите Ваше имя")
    #    self.bot.register_next_step_handler(msg, self.StartRouteName, number)
    
    def StartRouteName(self, message):
        msg = message.text
        curr = str(message.chat.id)
        self.message_route_name_signal.emit(curr, msg)
        self.bot.send_message(message.chat.id, "Информация направлена диспетчеру.\nХорошей смены!")


    def SendMessageToDispatcher(self, message):
        number = message.text
        curr = str(message.chat.id)
        self.message_signal.emit(curr, number)
        self.bot.send_message(message.chat.id, "Сообщение отправлено. Ожидайте, скоро с Вами свяжется диспетчер")
            

    def get_password(self, message):
        login = message.text
        msg = self.bot.send_message(message.chat.id, f'Логин: {login}\n❓ Введите пароль')
        self.bot.register_next_step_handler(msg, self.check_auth, login)

    def check_auth(self, message, login):
        try:
            print(message.chat.id)
            password = message.text
            cursor = self.conn.cursor()
            cursor.execute(" SELECT drivers_password FROM drivers WHERE drivers_login = %s ",
                        (login, ))
            db_password = cursor.fetchall()[0][0]
            cursor.execute(" SELECT drivers_login FROM drivers WHERE drivers_password = %s ",
                        (password, ))
            db_login = cursor.fetchall()[0][0]
            if login == db_login and password == db_password:
                cursor.execute("""
                    UPDATE drivers
                    SET telegram_id = %s
                    WHERE drivers_login = %s AND drivers_password = %s
                            """,
                    (message.chat.id, login, password))
                self.conn.commit()
                cursor.close()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton('Показать график📊')
                btn2 = types.KeyboardButton('Начать смену🚍')
                btn3 = types.KeyboardButton('Завершить смену🙅')
                btn4 = types.KeyboardButton('Сообщить о поломке💁‍♀️')
                btn5 = types.KeyboardButton('Сообщить о ДТП💀')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                self.bot.send_message(message.chat.id, '✅ Авторизация успешна!', reply_markup=markup)
            else:
                self.bot.send_message(message.chat.id, '❌ Неверный логин или пароль')
        except:
            self.bot.send_message(message.chat.id, "Неверный логин/пароль\nПопробуте еще раз(/start)")

#if __name__ == "__main__":
#    bus_bot = BusBot()
