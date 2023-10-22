import telebot
import re
import settings

BOT_TOKEN = settings.BOT_TOKEN
GROUP_ID = settings.GROUP_ID
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(content_types = ['text'])
def find_phone_number(message):
    if re.search(r'(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})', message.text):
        pass
    else:
        bot.send_message(message.chat.id, f'@{message.from_user.username} - ваше сообщение удалено. \n ▪️Чтобы отправить сообщение в нашем чате, добавьте номер телефона в объявление. \n ▪️Номер телефона указывать нужно начиная с +7, или 8. \n По рекламе писать сюда -  @Nikita_SOMIO22  \n(https://t.me/Nikita_SOMIO22)')
        bot.delete_message(message.chat.id, message.message_id)


if __name__ == '__main__':
    bot.infinity_polling()