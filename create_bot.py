from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5033193948:AAG4ftRIKhMVWaJnLEfdjaHDPDf_XSrChKc'

storage = MemoryStorage()

bot = Bot(token = TOKEN)

dp = Dispatcher(bot, storage = storage)
