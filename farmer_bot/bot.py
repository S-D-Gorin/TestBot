import telebot
import settings
import utils

BOT_TOKEN = settings.BOT_TOKEN
GROUP_ID = settings.GROUP_ID

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    # markup = telebot.types.InlineKeyboardMarkup()
    # button1 = telebot.types.InlineKeyboardButton("Посетить сайт", url='https://google.com')
    # button2 = telebot.types.InlineKeyboardButton("Сделать заказ", url='https://google.com')
    # button2 = telebot.types.InlineKeyboardButton("Сделать заказ", callback_data=utils.main_menu)
    # markup.add(button1, button2)
    # bot.send_message(message.chat.id, settings.FIRST_MESSAGE.format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, settings.FIRST_MESSAGE.format(message.from_user), reply_markup=utils.main_menu)
    
# bot.polling(none_stop=True)

    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
    

if __name__ == '__main__':
    bot.infinity_polling()