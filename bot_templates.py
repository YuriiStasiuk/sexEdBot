import asyncio
from aiogram import Bot, Dispatcher, executor, types

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
