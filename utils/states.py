from aiogram.fsm.state import StatesGroup, State


class Settings(StatesGroup):
    language = State()
    phone = State()
