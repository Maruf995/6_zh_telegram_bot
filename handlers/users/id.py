from aiogram import types
from loader import dp 

@dp.message_handler(text='/id')
async def command_start(message: types.Message):
    await message.answer(f'Твой айди: *{message.from_user.id}*',parse_mode= "Markdown")