
import logging
import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

# log level
logging.basicConfig(level=logging.INFO)

# init bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

""" aiogram is a synchronous library, so to have events to use callbacks, a 'callback' is
a reference to some functuion or a part of code that will be executed when the btn is pressed;
executed through '/random'
"""
button1 = InlineKeyboardButton(text='Random 1-10', callback_data='randomvalue_of10')
button2 = InlineKeyboardButton(text='Random 1-100', callback_data='randomvalue_of100')
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

# register basic commands
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply("Hi!\nI'm InitBot")

# handle '/random'
@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
	await message.reply('Select a range:', reply_markup=keyboard_inline)

# a handler for clicking the btns ()
@dp.callback_query_handler(text=['randomvalue_of10', 'randomvalue_of100'])
async def random_value(call: types.CallbackQuery):
	if call.data == 'randomvalue_of10':
		await call.message.answer(randint(1, 10))
	if call.data == 'randomvalue_of100':
		await call.message.answer(randint(1, 100))

	await call.answer()

# run long polling
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)