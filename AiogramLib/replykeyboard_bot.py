
import logging
import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

# bot level
logging.basicConfig(level=logging.INFO)

# init bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# variables for btns
button1 = KeyboardButton('👋button1')
button2 = KeyboardButton('💋YouTube')
button3 = KeyboardButton('🌈button3')
button4 = KeyboardButton('🍓button4')
""" a reply keyboard that contains the btns;
'resize_keyboard' - btns not to be very large, 'one_time_keyboard' - hide when a btn is pressed;
we can display a keyboard differetnly;
it's handled using '/start'
"""
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
	.add(button1).add(button2).add(button3).add(button4) # one btn in one line
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
	.add(button1, button2, button3, button4) # three btns in one line
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
	.row(button1, button2, button3, button4) # all the btns in one line
# in the current line has less than 3 btns, adds to the line, places on a new line otherwise
keyboard3.insert("INTERTED")

""" request a contact and location of the user;
it's handled using '/info'
"""
button5 = KeyboardButton('Who are you?', request_contact=True)
button6 = KeyboardButton('Where are you?', request_location=True)
keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) \
	.row(button5, button6)

# register basic commands 
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	"""
	Initiate the btns with '/start'
	"""
	await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=keyboard3)

# handle '/info'
@dp.message_handler(commands=['info'])
async def info(message: types.Message):
	await message.reply('Say something about you:', reply_markup=keyboard4)

# handle all text messages in the chat without filters
@dp.message_handler()
async def kb_answer(message: types.Message):
	if message.text == 'Hello!':
		await message.answer('Hi! Howdy?')
	elif message.text == 'YouTube':
		await message.answer('https://www.youtube.com/watch?v=HXVi2zT7l_c')
	else:
		await message.answer(f'Your message is {message.text}')


# run long polling
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)