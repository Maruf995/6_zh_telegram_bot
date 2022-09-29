from re import I
from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить Бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('id', 'узнать свой id')
    ])