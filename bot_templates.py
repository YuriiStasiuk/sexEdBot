from aiogram import Bot, Dispatcher, executor, types

def get_modules_list():
    pass
    #to do later

def modules_template():
    modules = get_modules_list()
    keyboard = types.InlineKeyboardMarkup()
    for i in modules:
        keyboard.add(types.InlineKeyboardButton(text="Модуль " + i[0], callback_data="select_module_" + i[1]))
    return keyboard
