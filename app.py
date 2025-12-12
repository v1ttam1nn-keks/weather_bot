import telebot

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
def handle_text








#Запуск бота
bot.polling()

#https://stepik.org/lesson/1396387/step/1?unit=1413255