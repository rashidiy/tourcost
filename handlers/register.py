import os
from gettext import gettext as _

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton
from database.models import User
from handlers.menu import prepare_menu
from loader import DP
from utils.states import Settings
from utils.translations import activate_language, get_all_versions


@DP.callback_query(F.data.in_(('uz:S', 'ru:S', 'uz', 'ru')))
async def select_language(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    user = await User.get_by_user_id(call.from_user.id)
    user.language = call.data.replace(':S', '')
    await user.commit()
    os.environ['LANG'] = user.language
    if call.data.endswith(':S'):
        await prepare_menu(call, state)
    else:
        await request_phone(call.message, state)


@DP.message(F.text.in_(get_all_versions('Edit Phone')))
@activate_language
async def request_phone(msg: Message, state: FSMContext):
    phone_btn = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_('Share my phone'), request_contact=True)]
    ], resize_keyboard=True)
    await msg.answer(_('Send your phone number'), reply_markup=phone_btn)
    await state.set_state(Settings.phone)


@DP.message(Settings.phone)
@activate_language
async def edit_phone(msg: Message, user: User, state: FSMContext):
    phone = (msg.text or msg.contact.phone_number).replace('+', '')
    if phone.isdigit():
        if phone.startswith('998') and len(phone) == 12:
            phone = '+' + phone
        elif len(phone) == 9:
            phone = '+998' + phone
    else:
        await request_phone(msg, state)
        return
    user.phone = phone
    await user.commit()
    await prepare_menu(msg, state)
    await state.clear()
