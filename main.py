import telebot

bot = telebot.TeleBot(key)

key = ""

def start():
    bot.polling()

if __name__ == '__main__':
    start()

