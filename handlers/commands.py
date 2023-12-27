from gettext import gettext as _

from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from app import DP
from database.models import User
from handlers.menu import prepare_menu
from utils.translations import activate_language, get_all_versions


@DP.message(CommandStart())
async def wel_come(msg: Message, state: FSMContext):
    user, created = await User.get_or_create(user_id=msg.from_user.id)
    if user.full_name != msg.from_user.full_name:
        user.full_name = msg.from_user.full_name
        await user.commit()

    if created:
        await language_selector(msg, settings=False)
    else:
        await prepare_menu(msg, state)


@DP.message(F.text.in_(get_all_versions('Language')))
@activate_language
async def language_selector(msg: Message, settings=True):
    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🇺🇿 O\'zbek tili 🇺🇿', callback_data='uz:S' if settings else 'uz')],
        [InlineKeyboardButton(text='🇷🇺 Русский 🇷🇺', callback_data='ru:S' if settings else 'ru')],
    ])
    await msg.answer(_('Select language'), reply_markup=buttons)
