import telebot
import requests
import json
bot = telebot.TeleBot('6056293518:AAE4hNBZu_LQH0yEgztEZ-LobJelJb3G7xE')
API = '98a2eed376eeee21863b4d556ea49d6c'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Рад тебя видеть! Напиши название города.')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

    else:
        bot.reply_to(message, 'Город указан неверно')

bot.polling(none_stop=True)


