import telebot
from telebot import types
from random import randint
from collections import defaultdict

token = '1297434940:AAHRuFcwYtWRU5qgFATA3w155L7Iwb_qZ1Y'
bot = telebot.TeleBot(token)

START, TITLE, PRICE, CONFIRMATION = range(4)
USER_STAGES = defaultdict(lambda: START)
products = defaultdict(lambda: {})
current_list = ['евро', 'доллар']
current_courses = {}


def get_stage(message):
    return USER_STAGES[message.chat.id]
def update_stage(message, state):
    USER_STAGES[message.chat.id] = state
def get_product(user_id):
    return products[user_id]
def update_product(user_id, key, value):
    products[user_id][key] = value


def create_currency_list():
    for cur in current_list:
        current_courses[cur] = randint(1, 100)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text=c, callback_data=c)
               for c in current_list]
    keyboard.add(*buttons)
    return keyboard


@bot.callback_query_handler(func=lambda x: True)
def callback_handler(callback_query):
    message = callback_query.message
    text = callback_query.data
    keyboard = create_keyboard()
    curens = get_currency_course(text)
    bot.answer_callback_query(callback_query.id, text=f'Курс {curens[0]} = {curens[1]}')
    bot.send_message(chat_id=message.chat.id, text=f'Курс {curens[0]} = {curens[1]}', reply_markup=keyboard)


def check_currency(message):
    for currenc in current_list:
        if currenc in message.text.lower():
            return True
    return False


def get_currency_course(text):
    for currency, course in current_courses.items():
        if currency in text.lower():
            return currency, course


def get_bank(location):
    lat = location.latitude
    lon = location.longitude
    bank_address = 'ул. Советская, 88'
    bank_lat, bank_lon = lat, lon
    return bank_address, bank_lat, bank_lon


@bot.message_handler(content_types=['location'])
def handle_location(message):
    print(message.location)
    bakn_addr, bank_lat, bank_lon = get_bank(message.location)
    bot.send_message(chat_id=message.chat.id, text=f'Вам нужен ближайший банк:\n{bakn_addr}')
    bot.send_location(chat_id=message.chat.id, latitude=bank_lat, longitude=bank_lon)


@bot.message_handler(func=check_currency)
def handle_currency(message):
    keyboard = create_keyboard()
    curens = get_currency_course(message.text)
    bot.send_message(chat_id=message.chat.id, text=f'Курс {curens[0]} = {curens[1]}', reply_markup=keyboard)


@bot.message_handler(func=lambda message: get_stage(message) == START)
def handle_message(message):
    bot.send_message(chat_id=message.chat.id, text='Напишите название')
    update_stage(message, TITLE)
@bot.message_handler(func=lambda message: get_stage(message) == TITLE)
def handle_title(message):
    update_product(message.chat.id, 'title', message.text)
    bot.send_message(chat_id=message.chat.id, text='Укажите цену товара')
    update_stage(message, PRICE)
@bot.message_handler(func=lambda message: get_stage(message) == PRICE)
def handle_price(message):
    update_product(message.chat.id, 'price', message.text)
    bot.send_message(chat_id=message.chat.id, text=f'Сохранить товар?\n {get_product(message.chat.id)}')
    update_stage(message, CONFIRMATION)
@bot.message_handler(func=lambda message: get_stage(message) == CONFIRMATION)
def handle_confirmation(message):
    if 'да' in message.text.lower():
        bot.send_message(chat_id=message.chat.id, text='Товар опубликован')
        product = get_product(message.chat.id)
        bot.send_message(chat_id=message.chat.id, text=f'{product["title"]}\n{product["price"]}\n')
    update_stage(message, START)

create_currency_list()
bot.polling()
