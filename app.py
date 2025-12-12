import telebot
from weather import add_base_in_dict
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
    
    if file_name.lower().endswith('.kml'):
        bot.reply_to(message, "THX, I WILL PARSE YOUR FILE")
        
        # Получаем информацию о файле
        file_info = bot.get_file(message.document.file_id)
        
        # Скачиваем файл
        downloaded_file = bot.download_file(file_info.file_path)
        # Сохраняем файл в текущей папке
        with open(file_name, 'wb') as f:
            f.write(downloaded_file)
        bot.reply_to(message, f'Done, {file_name} downloaded')
        kml_parse_form_botfile = add_base_in_dict(file_name)
        print(kml_parse_form_botfile)
        #bot.reply_to(message, f"<pre>{kml_parse_form_botfile}</pre>")
    else:
        bot.reply_to(message, "GO FUCK YOURSELF")

#Запуск бота
bot.polling()

#https://stepik.org/lesson/1396387/step/1?unit=1413255