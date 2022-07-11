
import logging
import config
from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# init bot (initialize bot and dispatcher)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# register 'start' command handler (interaction with a bot start with one command)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	""" 
	This handler will be called when user sends '/start' or '/help' command
	"""
	await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

# handle all text messages in the chat without filters
@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)

# run long polling
if __name__ == '__main__':
	# if the inf is too important, set the param to False
	executor.start_polling(dp, skip_updates=True)