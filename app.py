import gettext

import handlers
import asyncio
import logging

from database.database import db
from loader import DP, BOT


async def main():
    logging.basicConfig(level=logging.INFO)
    db.init()

    gettext.bindtextdomain('base', 'locales/')
    gettext.textdomain('base')

    for language in ["uz", "ru"]:
        language_translations = gettext.translation("base", "locales", languages=[language])
        language_translations.install()

        _ = language_translations.gettext

    await DP.start_polling(BOT)


if __name__ == '__main__':
    asyncio.run(main())
