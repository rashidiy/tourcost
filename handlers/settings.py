from aiogram import F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from gettext import gettext as _

from database.models import User
from loader import DP
from utils.translations import get_all_versions


@DP.message(F.text.in_(get_all_versions('Settings')))
async def settings(msg: Message):
    buttons = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_('Count of users'))],
        [KeyboardButton(text=_('Edit Phone'))],
        [KeyboardButton(text=_('Language')), KeyboardButton(text=_('Back'))],
    ], resize_keyboard=True)
    await msg.answer(_('Settings'), reply_markup=buttons)


@DP.message(F.text.in_(get_all_versions('Count of users')))
async def count_of_users(msg: Message):
    users = await User.get_all()
    await msg.answer(str(len(users)))
