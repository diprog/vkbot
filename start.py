"""
pip install python-telegram-bot
pip install requests
"""

import logging
from commands import commands
from telegram.ext import Updater
import utils

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    updater = Updater(utils.get_bot_token(), use_context=True, request_kwargs=utils.get_proxy())
    dp = updater.dispatcher

    # Подгружаем комманды из модуля commands.
    for handler in commands:
        dp.add_handler(handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()