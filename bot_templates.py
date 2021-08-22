import asyncio
from aiogram import Bot, Dispatcher, executor, types

def welcome_message():
    welcome_message = 'Привітальне повідомлення'
    return welcome_message, menu_keyboard()

def menu_keyboard():
    buttons = ['Показати модулі', 'Інший булшіт який зробимо в майбутньому']
    return types.ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)

def get_modules_list():
    modules = [['1', '1'], ['2', '2']]
    return modules


def modules_template():
    message_text = "Обери модуль"
    modules = get_modules_list()
    keyboard = types.InlineKeyboardMarkup()
    for i in modules:
        keyboard.add(types.InlineKeyboardButton(text="Модуль " + i[0], callback_data="select_module_" + i[1]))
    return message_text, keyboard
