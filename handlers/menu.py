from typing import Union

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, CallbackQuery
from gettext import gettext as _

from loader import DP
from utils.translations import activate_language, get_all_versions


@DP.message(F.text.in_(get_all_versions('Back')))
@activate_language
async def prepare_menu(update: Union[Message, CallbackQuery], state: FSMContext):
    buttons = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_('Contacts'))],
        [
            KeyboardButton(text=_('OpenSystem'), web_app=WebAppInfo(url='https://tourcost.uz')),
            KeyboardButton(text=_('Settings'))
        ],
    ], resize_keyboard=True)
    if isinstance(update, CallbackQuery):
        update = update.message
    await update.answer(_("Hello"), reply_markup=buttons)


@DP.message(F.text.in_(get_all_versions('Contacts')))
async def contacts(msg: Message):
    await msg.answer(_('Phone Contacts'))

print(get_all_versions('Contacts'))