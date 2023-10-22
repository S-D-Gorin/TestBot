import telebot
import re
import settings


BOT_TOKEN = settings.BOT_TOKEN
GROUP_ID = settings.GROUP_ID
bot = telebot.TeleBot(BOT_TOKEN)
DATABASES = {
    'bot': 'BM.txt',
    'correct': 'CM.txt',
    'uncorrect': 'UM.txt'
}

def db_write(db_name, mode, data):
    with open(db_name, mode=mode, encoding='utf-8') as db:
        db.write(data)

def db_read(db_name, mode, data_for_read):
    with open(db_name, mode=mode, encoding='utf-8') as db:
        pass



@bot.message_handler(content_types = ['text'])
def find_phone_number(message):
    if re.search(r'(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})', message.text):
        correct_message = f'{message.message_id} --- {message.from_user.username} --- {message.from_user.first_name} --- {message.text} \n'
        db_write(DATABASES.get('correct'), 'a', correct_message)
    else:
        uncorrect_message = f'{message.message_id} --- {message.from_user.username} --- {message.from_user.first_name} --- {message.text} \n'
        db_write(DATABASES.get('uncorrect'), 'a', uncorrect_message)

        bot.delete_message(message.chat.id, message.message_id)

        if message.from_user.username == None:
            user = message.from_user.first_name
        else:
            user = f'@{message.from_user.username}'
            
        message_id_to_del = bot.send_message(
            message.chat.id, 
            f'{user} - сообщение удалено.', 
            protect_content=True, 
            disable_notification=True
            ).message_id
        
        
        db_write(DATABASES.get('bot'), 'a', f'{str(message_id_to_del)}\n')
        
        with open(DATABASES.get('bot'), 'r', encoding='utf-8') as bot_message_id:
            message_id = bot_message_id.readlines()[-2]
            bot.delete_message(message.chat.id, int(message_id))
            if len(bot_message_id.readlines()) >= 10:
                db_write(DATABASES.get('bot'), 'w', str(message_id))












# @bot.message_handler(content_types = ['text'])
# def find_bot_message(message):
#     # pass
#     # if message.from_user.username in ['testbot-sdg9999', 'TestSdg9999Bot']:
#     OLD_MESSAGE = message.message_id
#     with open('db.txt', 'a', encoding='utf-8') as db:
#         # db.write(str(OLD_MESSAGE))
#         db.write('its work!')





if __name__ == '__main__':
    bot.infinity_polling()