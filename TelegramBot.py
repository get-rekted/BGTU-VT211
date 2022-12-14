import telebot
from telebot import types
import sqlite3
from time import sleep
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot('2092911505:AAFRH-4mTvJlgq_9xogDUFXX86ucAxb63O0')

@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Crypto 📈')
    button2 = types.KeyboardButton('USD to 📊')
    button3 = types.KeyboardButton('FAQ 📌')
    button4 = types.KeyboardButton('Feedback 🔥')
    button5 = types.KeyboardButton('News 🗣')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}. '
                                      'Я рад тебя видеть! :)\n'
                                      '\nЧто хочешь узнать?\n\n<b>Список команд:</b>\n \nCrypto — узнать актуальный курс 10 самых популярных криптовалют в ' \
                                      'мире\nUSD to — узнать курс доллара по отношению к RUB, EUR, UAH\nFAQ — ответы на вопросы\nFeedback — написать ' \
                                      'сообщение создателю бота\nNews — узнать последние новости из мира криптовалют (последние 5 актуальных статей с сайта CoinDesk)'.format(message.from_user), reply_markup=markup,
                     parse_mode='HTML')
    # создаем БД
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""")
    connect.commit()

    # проверка id на повтор
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    print(data)
    if data is None:
        # добавляем значение
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()


# Команда для удаления юзера из БД
@bot.message_handler(commands=['delete_me_from_db'])
def delete(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    # удаление из БД
    people_id = message.chat.id
    cursor.execute(f"DELETE FROM login_id WHERE id = {people_id}")
    connect.commit()
    print('Удалил юзера из БД')

@bot.message_handler(commands=['help'])
def hlbot(message):
    bot.send_message(message.chat.id, 'Тех. поддержка - @durov')

cg = CoinGeckoAPI()

# Кнопка просмотра курса криптовалют

# CRYPTO
price = cg.get_price(ids='bitcoin,litecoin,ethereum,terra-luna,solana,ripple,polkadot,dogecoin,chainlink',
                     vs_currencies='usd')
crypto = f"Bitcoin (BTC) — {price['bitcoin']['usd']:.2f}$" \
         + f"\nLitecoin (LTC) — {price['litecoin']['usd']:.2f}$" \
         + f"\nEthereum (ETH) — {price['ethereum']['usd']:.2f}$" \
         + f"\nTerra (LUNA) — {price['terra-luna']['usd']:.2f}$" \
         + f"\nSolana (SOL) — {price['solana']['usd']:.2f}$" \
         + f"\nXRP (XRP) — {price['ripple']['usd']:.2f}$" \
         + f"\nPolkadot (DOT) — {price['polkadot']['usd']:.2f}$" \
         + f"\nDogecoin (DOGE) — {price['dogecoin']['usd']:.2f}$" \
         + f"\nChainlink (LINK) — {price['chainlink']['usd']:.2f}$" \

course = convert(amount=1, to=['RUB', 'EUR', 'UAH'])
usd = f"1 USD = {course['RUB']} RUB" \
      + f"\n1 USD = {course['EUR']} EUR" \
      + f"\n1 USD = {course['UAH']} UAH"

# Парсер

url = "https://www.coindesk.com/"
request = requests.get(url)
bs = BeautifulSoup(request.text, "html.parser")

all_links = bs.find_all("a", class_="headline", limit=5)

@bot.message_handler(content_types=['text'])
def send_message_handler(message):
    if message.chat.type == 'private':

        # CRYPTO
        if message.text == "Crypto 📈":
            bot.send_message(message.chat.id, crypto)

        # USD
        elif message.text == 'USD to 📊':
            bot.send_message(message.chat.id, usd)

        # FAQ
        elif message.text == 'FAQ 📌':
            bot.send_message(message.chat.id,
                             '<b>Ответы на вопросы:</b>\n\n 1) С какого сайта бот берет цены? - С сайта CoinGecko.\n\n 2) Почему CoinGecko? - '
                             'Ежеминутное обновление курса монет и наличие API.\n\n 3) Как пришла идея о создании данного бота? - '
                             'Спонтанно.', parse_mode='HTML')

        # FEEDBACK
        elif message.text == 'Feedback 🔥':
            bot.send_message(message.chat.id, '<b>Создатель бота</b> - Get Rekted \n\n VK - @durov\n\n TG - @durov',
                             parse_mode='HTML')

        elif message.text == 'News 🗣':
            for link in all_links:
                bot.send_message(message.chat.id, "https://www.coindesk.com/" + link["href"])


        else:
            bot.send_message(message.chat.id,
                             'Такой команды не существует. Напишите — /start — чтобы узнать список существующих команд.')

print('Бот вышел в online!')
bot.polling()