import telebot
import config
from exel_in_pandas import name_table, conver_xlsx

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def start(message):
    text = 'Пришлите файл'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['document'])
def xlsx(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = r'test/' + name_table()[0];
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, conver_xlsx())
    except Exception:
        bot.send_message(message.chat.id, 'Что-то пошло не так')



bot.polling(none_stop=True)
