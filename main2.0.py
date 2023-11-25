import serial
from telebot import *
from time import sleep
Sudo = input("sudo: ")
port = None
while True:
    if port != None:
        break
    else:
        pass
    try:
        port = int(input("please enter the port number where the device is connected:  "))
    except:
        port = None

big_svet = "❌"
stol_svet = "❌"
rgb_svet = "❌"
loop_svet = "❌"
roz_stol = "❌"
roz_stan = "❌"
roz_bp = "❌"
Password = False
error_bot = 0

UserTrue = []
Master = []
RootUser = []

try:
   ArduinoSerial = serial.Serial(('com'+str(port)), 9600)
   sleep(1)
except:
   print("отсутствует устройство на com"+str(port))

try:
    if error_bot == 0:
        print("подключение стабильно")
    bot = telebot.TeleBot('6604896635:AAEYvcBPvbE1YwrdZbmbv77xu-R9G_hypss')


    @bot.message_handler(commands=["start"])
    def start(message):
        print(message.from_user.id)
        bot.send_message(message.from_user.id, "Привет, я бот твоего умного дома!"
                                               "\nДавай авторезируемся что бы я тебя узнал🥸"
                                               "\n"
                                               "\nВведите пароль")
        #bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        #bot.delete_message(message.chat.id, message.message_id)
    @bot.message_handler(func=lambda message: message.text == "назад")
    def Exit(message):
        password(message)
    @bot.message_handler(func=lambda message: message.text == "💡свет💡")
    def Svet(message):
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                sanes = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn5 = types.KeyboardButton("💡Большой💡")
                btn6 = types.KeyboardButton('💡Настольный💡')
                btn7 = types.KeyboardButton("💡RGB лента💡")
                btn8 = types.KeyboardButton('💡Лупа💡')
                btn9 = types.KeyboardButton('назад')
                sanes.add(btn5)
                sanes.add(btn6)
                sanes.add(btn7)
                sanes.add(btn8)
                sanes.add(btn9)
                bot.send_message(message.from_user.id, "💡свет управление💡", reply_markup=sanes)
                break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
            pass
    @bot.message_handler(func=lambda message: message.text == "⚡️розетки⚡️")
    def Rozetka(message):
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                rozet = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn10 = types.KeyboardButton("⚡️стол⚡️")
                btn11 = types.KeyboardButton('⚡️станция⚡️')
                btn12 = types.KeyboardButton("⚡️блок питания⚡️")
                btn13 = types.KeyboardButton('назад')
                rozet.add(btn10)
                rozet.add(btn11)
                rozet.add(btn12)
                rozet.add(btn13)
                bot.send_message(message.from_user.id, '⚡️управление розетками⚡️', reply_markup=rozet)
                break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
            pass
    @bot.message_handler(func=lambda message: message.text == "💡Большой💡")
    def RL1(message):
        global big_svet
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                if big_svet == "❌":
                    ArduinoSerial.write(bytes([201]))
                    big_svet = "✅"
                else:
                    ArduinoSerial.write(bytes([211]))
                    big_svet = "❌"
                    break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
            pass
        password(message)
    @bot.message_handler(func=lambda message: message.text == "💡Настольный💡")
    def RL2(message):
        global stol_svet
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                if stol_svet == "❌":
                    ArduinoSerial.write(bytes([202]))
                    stol_svet = "✅"
                else:
                    ArduinoSerial.write(bytes([212]))
                    stol_svet = "❌"
                break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
            pass
        password(message)
    @bot.message_handler(func=lambda message: message.text == "💡RGB лента💡")
    def RL3(message):
        global rgb_svet
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                if rgb_svet == "❌":
                    ArduinoSerial.write(bytes([203]))
                    rgb_svet = "✅"
                else:
                    ArduinoSerial.write(bytes([213]))
                    rgb_svet = "❌"
                password(message)
                break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
            pass
    @bot.message_handler(func=lambda message: message.text == "💡Лупа💡")
    def RL4(message):
        global loop_svet
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                if loop_svet == "❌":
                    ArduinoSerial.write(bytes([204]))
                    loop_svet = "✅"
                else:
                    ArduinoSerial.write(bytes([214]))
                    loop_svet = "❌"
            password(message)
            break
        else:
            pass
        if UserFalse == True:
            password(message)
        else:
            pass
    @bot.message_handler(func=lambda message: message.text == "⚡️стол⚡️")
    def RL5(message):
        global roz_stol
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                try:
                    if roz_stol == "❌":
                        ArduinoSerial.write(bytes([101]))
                        roz_stol = "✅"
                    else:
                        ArduinoSerial.write(bytes([111]))
                        roz_stol = "❌"
                    password(message)
                except:
                    bot.send_message(message.from_user.id, "⚙️модуль SNH не обноружен⚙️")
                break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
            pass
    @bot.message_handler(func=lambda message: message.text == "⚡️станция⚡️")
    def RL6(message):
        global roz_bp
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                try:
                    if roz_bp == "❌":
                        ArduinoSerial.write(bytes([102]))
                        roz_bp = "✅"
                    else:
                        ArduinoSerial.write(bytes([112]))
                        roz_bp = "❌"
                    password(message)
                except:
                    bot.send_message(message.from_user.id, "⚙️модуль SNH не обноружен⚙️")
                break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
            pass
    @bot.message_handler(func=lambda message: message.text == "⚡️блок питания⚡️")
    def RL7(message):
        global roz_stan
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                try:
                    if roz_stan == "❌":
                        ArduinoSerial.write(bytes([103]))
                        roz_stan = "✅"
                    else:
                        ArduinoSerial.write(bytes([113]))
                        roz_stan = "❌"
                    password(message)
                except:
                    bot.send_message(message.from_user.id, "⚙️модуль SNH не обноружен⚙️")
                break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
                pass
    @bot.message_handler(func=lambda message: message.text == "off all")
    def OffAll(message):
        global big_svet
        global stol_svet
        global rgb_svet
        global loop_svet
        global roz_stol
        global roz_stan
        global roz_bp
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                UserFalse = False
                try:
                    ArduinoSerial.write(bytes([211]))
                    ArduinoSerial.write(bytes([212]))
                    ArduinoSerial.write(bytes([213]))
                    ArduinoSerial.write(bytes([214]))
                    ArduinoSerial.write(bytes([111]))
                    ArduinoSerial.write(bytes([112]))
                    ArduinoSerial.write(bytes([113]))
                except:
                    bot.send_message(message.from_user.id, "⚙️модуль SNH не обноружен⚙️")
                roz_stol = "❌"
                roz_bp = "❌"
                roz_stan = "❌"
                stol_svet = "❌"
                big_svet = "❌"
                rgb_svet = "❌"
                loop_svet = "❌"
                password(message)
                break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
                pass
    @bot.message_handler(func=lambda message: message.text == "Off")
    def Off(message):
        global UserFalse
        UserFalse = True
        for User in UserTrue:
            if User == message.from_user.id:
                pass
                break
            else:
                pass
        if UserFalse == True:
            password(message)
        else:
            pass


    @bot.message_handler(content_types=["text"])
    def password(message):
        print(message.text)
        global UserFalse
        UserFalse = True
        if message.text == "User":
            UserTrue.append(message.from_user.id)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💡свет💡")
            btn2 = types.KeyboardButton('⚡️розетки⚡️')
            btn4 = types.KeyboardButton('📴отключить📴')
            btn20 = types.KeyboardButton("off all")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn4)
            markup.add(btn20)
            bot.send_message(message.from_user.id, "🖥Управление🖥"
                                                   "\n"
                                                   "\nСвет💡"
                                                   "\nБольшой        " + str(big_svet) +
                                                   "\nНастольный  " + str(stol_svet) +
                                                   "\nRGB лента      " + str(rgb_svet) +
                                                   "\nЛупа                " + str(loop_svet) +
                                                   "\n"
                                                   "\nРозетки⚡️"
                                                   "\nСтол                   " + str(roz_stol) +
                                                   "\nСтанция            " + str(roz_stan) +
                                                   "\nБлок Питания  " + str(roz_bp), reply_markup=markup)
        elif message.text != "User":
            for User in UserTrue:
                if User == message.from_user.id:
                    UserFalse = False
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn1 = types.KeyboardButton("💡свет💡")
                    btn2 = types.KeyboardButton('⚡️розетки⚡️')
                    btn4 = types.KeyboardButton('📴отключить📴')
                    btn20 = types.KeyboardButton("off all")
                    markup.add(btn1)
                    markup.add(btn2)
                    markup.add(btn4)
                    markup.add(btn20)
                    bot.send_message(message.from_user.id, "🖥Управление🖥"
                                                           "\n"
                                                           "\nСвет💡"
                                                           "\nБольшой        " + str(big_svet) +
                                                           "\nНастольный  " + str(stol_svet) +
                                                           "\nRGB лента      " + str(rgb_svet) +
                                                           "\nЛупа                " + str(loop_svet) +
                                                           "\n"
                                                           "\nРозетки⚡️"
                                                           "\nСтол                   " + str(roz_stol) +
                                                           "\nСтанция            " + str(roz_stan) +
                                                           "\nБлок Питания  " + str(roz_bp), reply_markup=markup)
                    break
                else:
                    pass
            if UserFalse == True:
                bot.send_message(message.from_user.id, "Неправильно введён пароль!")
                bot.register_next_step_handler(message, password)
            else:
                pass
        else:
            pass


    bot.polling(none_stop=True, )
except:
    error_bot = 1
    print("error, отсутствует подключение к интернету")
    sleep(1)






