from telegram import InlineKeyboardMarkup
from interface.buttons import *


def Start():
    return InlineKeyboardMarkup([[ConnectVK()]])