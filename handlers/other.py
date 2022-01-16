from aiogram import types, Dispatcher
from create_bot import dp, bot

# @dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Ты что бухой':
        await bot.send_message(message.from_user.id, 'Нет')
    else:
        await bot.send_message(message.from_user.id, 'Нет такой команды')

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)