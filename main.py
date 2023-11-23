import serial
from telebot import *
from time import sleep
port = 5
try:
   ArduinoSerial = serial.Serial(('com'+str(port)), 9600)
   sleep(1)
except:
   print("отсутствует устройство на com"+str(port))

big_svet = "❌"
stol_svet = "❌"
rgb_svet = "❌"
loop_svet = "❌"
roz_stol = "❌"
roz_stan = "❌"
roz_bp = "❌"
error = 0
error_bot = 0
UserPassword = 0
Users = []


users = ["", ""]

try:
    if error_bot == 0:
        print("подключение стабильно")
    bot = telebot.TeleBot('6604896635:AAEYvcBPvbE1YwrdZbmbv77xu-R9G_hypss')



    @bot.message_handler(commands=['start'])
    def user(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("💡свет💡")
        btn2 = types.KeyboardButton('⚡️розетки⚡️')
        btn4 = types.KeyboardButton('📴отключить📴')
        btn20 = types.KeyboardButton("off all")
        markup.add(btn1, btn2, btn4, btn20)
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



    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):

        print(message.text)
        if message.text == "💡свет💡":
            sanes = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn5 = types.KeyboardButton("💡Большой💡")
            btn6 = types.KeyboardButton('💡Настольный💡')
            btn7 = types.KeyboardButton("💡RGB лента💡")
            btn8 = types.KeyboardButton('💡Лупа💡')
            btn9 = types.KeyboardButton('назад')
            sanes.add(btn5, btn6, btn7, btn8, btn9)
            bot.send_message(message.from_user.id, "💡свет управление💡", reply_markup=sanes)
        elif message.text == "⚡️розетки⚡️":
            rozet = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn10 = types.KeyboardButton("⚡️стол⚡️")
            btn11 = types.KeyboardButton('⚡️станция⚡️')
            btn12 = types.KeyboardButton("⚡️блок питания⚡️")
            btn13 = types.KeyboardButton('назад')
            rozet.add(btn10, btn11, btn12, btn13)
            bot.send_message(message.from_user.id, '⚡️управление розетками⚡️', reply_markup=rozet)  # ответ бота
        elif message.text == "📴отключить📴":
            off = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn18 = types.KeyboardButton("да отключить")
            btn19 = types.KeyboardButton('назад')
            off.add(btn18, btn19)
            bot.send_message(message.from_user.id, 'вы уверены что хотите отключить систему Smart Neon Home?', reply_markup=off)

        # свет
        elif message.text == "💡Большой💡":
            global big_svet
            if big_svet == "❌":
                ArduinoSerial.write(bytes([201]))
                big_svet = "✅"
            else:
                ArduinoSerial.write(bytes([211]))
                big_svet = "❌"
            user(message)
        elif message.text == "💡Настольный💡":
            global stol_svet
            if stol_svet == "❌":
                ArduinoSerial.write(bytes([202]))
                stol_svet = "✅"
            else:
                ArduinoSerial.write(bytes([212]))
                stol_svet = "❌"
            user(message)
        elif message.text == "💡RGB лента💡":
            global rgb_svet
            if rgb_svet == "❌":
                ArduinoSerial.write(bytes([203]))
                rgb_svet = "✅"
            else:
                ArduinoSerial.write(bytes([213]))
                rgb_svet = "❌"
            user(message)
        elif message.text == "💡Лупа💡":
            global loop_svet
            if loop_svet == "❌":
                ArduinoSerial.write(bytes([204]))
                loop_svet = "✅"
            else:
                ArduinoSerial.write(bytes([214]))
                loop_svet = "❌"
            user(message)
        # розетки

        elif message.text == "⚡️стол⚡️":
            global roz_stol
            if roz_stol == "❌":
                ArduinoSerial.write(bytes([101]))
                roz_stol = "✅"
            else:
                ArduinoSerial.write(bytes([111]))
                roz_stol = "❌"
            user(message)
        elif message.text == "⚡️блок питания⚡️":
            global roz_bp
            if roz_bp == "❌":
                ArduinoSerial.write(bytes([102]))
                roz_bp = "✅"
            else:
                ArduinoSerial.write(bytes([112]))
                roz_bp = "❌"
            user(message)
        elif message.text == "⚡️станция⚡️":
            global roz_stan
            if roz_stan == "❌":
                ArduinoSerial.write(bytes([103]))
                roz_stan = "✅"
            else:
                ArduinoSerial.write(bytes([113]))
                roz_stan = "❌"
            user(message)
        # SNH
        elif message.text == "назад":
            user(message)
        elif message.text == "да отключить":
            pass
        elif message.text == "off all":
            ArduinoSerial.write(bytes([211]))
            ArduinoSerial.write(bytes([212]))
            ArduinoSerial.write(bytes([213]))
            ArduinoSerial.write(bytes([214]))
            ArduinoSerial.write(bytes([111]))
            ArduinoSerial.write(bytes([112]))
            ArduinoSerial.write(bytes([113]))
            roz_stol = "❌"
            roz_bp = "❌"
            roz_stan = "❌"
            stol_svet = "❌"
            big_svet = "❌"
            rgb_svet = "❌"
            loop_svet = "❌"
            user(message)
        else:
            bot.send_message(message.from_user.id, "нет такой дерриктории")  # ответ бота

    bot.polling(none_stop=True)
    error_bot = 0

except:
    error_bot = 1
    print("error, отсутствует подключение к интернету")
    sleep(1)

