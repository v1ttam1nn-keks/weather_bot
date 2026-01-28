import telebot
from weather import add_base_in_dict
import os
#Создание Экземпляра бота
bot = telebot.TeleBot('7525203380:AAGfPBAaHXJfN0Y5_XBRH5ZUCjqVeIQoUKE')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "HUYTAM")

@bot.message_handler(commands=['help', 'about'])
def help_command(message):
    bot.reply_to(message,"ANY SOSAL?!?")

#@bot.message_handler(commands=['help'])
#def help_command(message):
#    bot.reply_to(message,"ANY QUESTIONS!?")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    response = f'You send me: {message.text}'
    bot.send_message(message.chat.id, response)

@bot.message_handler(content_types=['document'])
def check_and_download(message):
    file_name = message.document.file_name

    if not file_name.lower().endswith('.kml'):
        bot.reply_to(message, "GO FUCK YOURSELF")
        return

    bot.reply_to(message, "THX, I WILL PARSE YOUR FILE")

    SAVE_DIR = 'downloads'
    os.makedirs(SAVE_DIR, exist_ok=True)
    save_path = os.path.join(SAVE_DIR, file_name)

    try:
        # скачать
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(save_path, 'wb') as f:
            f.write(downloaded_file)

        # парсинг
        kml_data = add_base_in_dict(save_path)
        print(kml_data)

        # если дошли сюда — значит ошибок не было
        os.remove(save_path)

        bot.reply_to(message, "KML parsed successfully, file removed")

    except Exception as e:
        # если ошибка — файл НЕ удаляем
        bot.reply_to(message, "ERROR while parsing KML")
        print("KML PARSE ERROR:", e)

#Запуск бота
bot.polling()

#https://stepik.org/lesson/1396387/step/1?unit=1413255