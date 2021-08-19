import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.builtin import Text
logging.basicConfig(level=logging.INFO)
from os import getenv
from sys import exit
from bot_templates import modules_keyboard

"""getting bot token from env - for secutiry reasons"""
bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token = bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    #add user to database
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)   #to change this - so this markup can be getted using some method
    buttons = ['Показати модулі', 'Інший булшіт який зробимо в майбутньому']
    poll_keyboard.add(*buttons)
    await message.answer("Привітальне повідомлення", reply_markup=poll_keyboard)

@dp.message_handler(lambda message: message.text == "Показати модулі")
async def modules_list(message: types.Message):
    modules = [["Назва модулю", "Ідентифікатор модулю"], ['назва іншого модулю', "ідентифікатор іншого модулю"]]
    keyboard = types.InlineKeyboardMarkup()
    for i in modules:
        keyboard.add(types.InlineKeyboardButton(text="Модуль " + i[0], callback_data="select_module_"+i[1]))
    await message.reply(text = "Ось це треба буде пофіксити", reply_markup=types.ReplyKeyboardRemove())   #to fix later
    await message.answer("Обери модуль", reply_markup=keyboard)

@dp.callback_query_handler(Text(startswith="select_module_"))
async def callback_module(call: types.CallbackQuery):
    identifier = call.data.split("_")[2]
    #to write a method that will check whether a person have previously completed this module
    #to write a method that will get a message with the module
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Почати модуль", callback_data="start_module_"))
    keyboard.add(types.InlineKeyboardButton(text="Скасувати", callback_data="cancel_selection"))
    await call.message.answer(text = "Вітаємо в модулі " + identifier + ". Тут буде більше інформації трішки про те що знаходиться в модулі", reply_markup = keyboard)
    await call.answer()

@dp.callback_query_handler(Text(startswith="start_module_"))
async def callback_start(call: types.CallbackQuery):
    identifier = call.data.split("_")[2]
    #to add method that will get a message with the first study block
    #to create some sort of identifiers
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Продовжити", callback_data="continue"))   #to add some identifier here
    await call.message.answer(text='Ще не готово', reply_markup=keyboard)
    await call.message.delete()
    await call.answer()

@dp.callback_query_handler(Text(startswith="continue"))
async def callback_continue(call: types.CallbackQuery):
    #to do a lot
    await call.answer("Not done yet", show_alert=True)

@dp.callback_query_handler(Text(startswith="cancel_selection"))
async def cancel_selection(call: types.CallbackQuery):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # to change this - so this markup can be getted using some method
    buttons = ['Показати модулі', 'Інший булшіт який зробимо в майбутньому']
    poll_keyboard.add(*buttons)
    await call.message.answer("Тут будуть якісь слова", reply_markup=poll_keyboard)
    await call.message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

