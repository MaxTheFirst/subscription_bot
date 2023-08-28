from config import BOT_TOKEN
from user_timer import UserTimer
from db import DBManager
from bot_filters import IsAdmin, CallbackCmd
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.bind_filter(IsAdmin)
dp.bind_filter(CallbackCmd)

timer = UserTimer()

DBManager.start()