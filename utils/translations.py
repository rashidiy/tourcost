import gettext
import inspect
import os
from typing import Union

from aiogram.types import Message, CallbackQuery
from aiogram.utils.mypy_hacks import lru_cache

from database.models import User


def has_parameter(func, param_name):
    """
    Check if a function has a parameter with the specified name.
    """
    signature = inspect.signature(func)
    return param_name in signature.parameters


def activate_language(func):
    async def wrapper(update: Union[Message | CallbackQuery], *args, **kwargs):
        user = update.from_user
        obj = await User.get_by_user_id(user.id)
        if obj and obj.language:
            os.environ['LANG'] = obj.language
        kw = {p: v for p, v in kwargs.items() if has_parameter(func, p)}
        if has_parameter(func, 'user'):
            if not obj:
                raise f'User not found {user.id}'
            kw['user'] = obj
        return await func(update, *args, **kw)

    return wrapper


@lru_cache
def get_all_versions(s: str):
    translations = []

    for language in ['uz', 'ru']:
        language_translations = gettext.translation("base", "locales", languages=[language])
        language_translations.install()
        _ = language_translations.gettext
        translations.append(str(_(s)))

    return translations
