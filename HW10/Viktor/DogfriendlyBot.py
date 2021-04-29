import telebot
from telebot import types
from pyowm import OWM

bot = telebot.TeleBot("1795901906:AAER1b0zciszipG3ByvOvZAgvq3G8-gunzE")
owm = OWM('ff4f133de218c34ec948c86be2fb8b1a')
mgr = owm.weather_manager()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    send_mesage = f"<b>Привіт {message.from_user.first_name}</b>!\nЩо робить цей бот?\n\nDogfriendlyBot любить собак.\nВін допоможе вирішити проблеми,\nякі виникають у догляді за чотирилапими.\n\nДля додаткової інформації /help"
    bot.send_message(message.chat.id, send_mesage, parse_mode='html')

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, "/weather - що коїться за вікном сьогодні ⛅\n\
/games - веселі ігри разом 🥎\n\
/toys - іграшки для собак 🦴\n\
/treats - поповнити запаси енергії 🍗\n\
/food - основна їжа 🥩")

@bot.message_handler(commands=['weather'])
def selected_weather(message):
    message.text = "Львів"
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temperature = w.temperature('celsius')
    answer = f"Температура у місті {message.text} {temperature['temp']}, вологість {w.humidity} %"
    bot.send_message(message.chat.id, answer)

#"Hello, it's a perfect day for a walk with your dog 😉"

@bot.message_handler(commands=['games'])
def selected_toys(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://hvost.news/animals/dogs-games/samye-interesnye-igry-s-sobakoy/"))
    bot.send_message(message.chat.id,
                     "Натисніть на кнопку, щоб переглянути варіанти ігор",
                     parse_mode="html", reply_markup=markup)

@bot.message_handler(commands=['toys'])
def selected_toys(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://ezoo.com.ua/uk/igrushki-dlya-sobak-c-18597_18604.html"))
    bot.send_message(message.chat.id,
                     "Натисніть на кнопку, щоб вибрати в магазині",
                     parse_mode="html", reply_markup=markup)

@bot.message_handler(commands=['treats'])
def selected_toys(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://pethouse.ua/ua/shop/sobakam/lakomstva-i-kosti/"))
    bot.send_message(message.chat.id,
                     "Натисніть на кнопку, щоб вибрати в магазині",
                     parse_mode="html", reply_markup=markup)

@bot.message_handler(commands=['food'])
def selected_toys(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://masterzoo.ua/ua/catalog/sobaki/korm-dlya-sobak/"))
    bot.send_message(message.chat.id,
                     "Натисніть на кнопку, щоб вибрати в магазині",
                     parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)


#@bot.message_handler(func=lambda message: True, content_types=['text'])
#def command_default(message):
#    bot.send_message(message.chat.id, "Я не розумію \"" + message.text + "\"\nДля довідки /help")

bot.polling()
