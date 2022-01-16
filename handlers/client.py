from aiogram import types, Dispatcher
from create_bot import dp, bot
from keybords import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# @dp.message_handler(commands = ['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, "Привет!", reply_markup=kb_client)

# @dp.message_handler(commands = ['Режим_работы'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, '24/7')

# @dp.message_handler(commands = ['Меню'])
async def menu_command(message : types.Message):
    await message.answer("Высылаю меню в личку")
    await sqlite_db.sql_read(message)

# @dp.message_handler(commands = ['Расположение'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Elenberg, ST-675')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands = ['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands = ['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands = ['Расположение'])
    dp.register_message_handler(menu_command, commands = ['Меню'])
    