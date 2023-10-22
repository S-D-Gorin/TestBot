import telebot
import settings


BOT_TOKEN = settings.BOT_TOKEN
GROUP_ID = settings.GROUP_ID

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
    
    

if __name__ == '__main__':
    bot.infinity_polling()