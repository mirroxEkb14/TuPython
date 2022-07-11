
import logging
import config
import pyqrcode
from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# init bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# register 'start' command handler
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

# send images (when user sends '/logo')
@dp.message_handler(commands=['logo'])
async def send_image(message: types.Message):
	await message.answer_photo('https://www.gettyimages.de/gi-resources/images/500px/983794168.jpg')

# handle all text messages in the chat without filters
@dp.message_handler()
async def qr(message: types.Message):
	"""
	Download 'pyqrcode' library
	Download 'pypng' library to use .png method
	"""
	text = pyqrcode.create(message.text) # generate a qr-code of messages
	text.png('code.png', scale=5) # save qr images to a local drive (5x5 pixels)
	await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb')) # read binary mode

# run long polling
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)