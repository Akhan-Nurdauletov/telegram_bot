from aiogram import types, Dispatcher
from create_bot import dp, bot
from keybords import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text


# @dp.message_handler(commands = ['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, "Привет!", reply_markup=kb_client)

# @dp.message_handler(commands = ['Режим_работы'])
# @dp.message_handler(Text(equals = 'Режим работы', ignore_case = True))
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, '24/7')

# @dp.message_handler(commands = ['Меню'])
# @dp.message_handler(Text(equals = 'Меню', ignore_case = True))
async def menu_command(message : types.Message):
    await message.answer("Высылаю меню в личку")
    await sqlite_db.sql_read(message)

# @dp.message_handler(commands = ['Расположение'])
# @dp.message_handler(Text(equals = 'Расположение', ignore_case = True))
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Elenberg, ST-675')

# @dp.message_handler(commands = ['Контакты'])
# @dp.message_handler(Text(equals = 'Контакты', ignore_case = True))
async def contacts_command(message : types.Message):
    await bot.send_message(message.from_user.id, '+ 7 777 777 77 77')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands = ['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands = ['Режим_работы'])
    dp.register_message_handler(pizza_open_command, Text(equals = 'Режим работы', ignore_case = True))
    dp.register_message_handler(pizza_place_command, commands = ['Расположение'])
    dp.register_message_handler(pizza_place_command, Text(equals = 'Расположение', ignore_case = True))
    dp.register_message_handler(menu_command, commands = ['Меню'])
    dp.register_message_handler(menu_command, Text(equals = 'Меню', ignore_case = True))
    dp.register_message_handler(contacts_command, commands = ['Контакты'])
    dp.register_message_handler(contacts_command, Text(equals = 'Контакты', ignore_case = True))