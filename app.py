API_TOKEN = '7525203380:AAGfPBAaHXJfN0Y5_XBRH5ZUCjqVeIQoUKE'

"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['sticker'])
async def reply_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)

@dp.message_handler(content_types=['document'])
async def download_kml_file(message: types.Message)


@dp.message_handler(commands = ['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMiaRxPFakCHbG5XJ5sf7Sm7XZp6MAAAnNtAAIzG6FI4XIEowaGm1o2BA')
    await message.reply("Hello! Send me a KML file and wait")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



