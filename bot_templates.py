import asyncio
from aiogram import Bot, Dispatcher, executor, types

async def get_modules_list():
    module = {'1': 1,'2': 2}
    return module


async def modules_template():
    message_text = "Обери модуль"
    modules = asyncio.run(get_modules_list())
    keyboard = types.InlineKeyboardMarkup()
    for i in modules:
        keyboard.add(types.InlineKeyboardButton(text="Модуль " + i[0], callback_data="select_module_" + i[1]))
    return message_text, keyboard


# modules = [["Назва модулю", "Ідентифікатор модулю"], ['назва іншого модулю', "ідентифікатор іншого модулю"]]
 #   keyboard = types.InlineKeyboardMarkup()
  #  for i in modules:
   #     keyboard.add(types.InlineKeyboardButton(text="Модуль " + i[0], callback_data="select_module_"+i[1]))
    #await message.reply(text = "Ось це треба буде пофіксити", reply_markup=types.ReplyKeyboardRemove())   #to fix later
    #await message.answer("Обери модуль", reply_markup=keyboard)