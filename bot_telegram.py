from asyncore import dispatcher
from aiogram.utils import executor
from create_bot import dp, bot
import config
import os
from data_base import sqlite_db

async def on_startup(dp):
    print('Бот онлайн')
    sqlite_db.sql_start()
    # await bot.set_webhook(config.URL_APP)

# async def on_shutdown(dp):
#     await bot.delete_webhook()

from handlers import admin, client, other

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
other.register_handlers_other(dp)


if __name__ =='__main__':
    executor.start_polling(dp, on_startup=on_startup)
    # executor.start_webhook(
    #     dispatcher = dp,
    #     webhook_path = '',
    #     on_startup = on_startup,
    #     on_shutdown = on_shutdown,
    #     skip_updates = True,
    #     host = "0.0.0.0",
    #     port = int(os.environ.get("PORT", 5000))
    # )
