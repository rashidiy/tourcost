import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

BOT = Bot(os.getenv('BOT_TOKEN'))
storage = MemoryStorage()
DP = Dispatcher(storage=storage)
