from telegram import InlineKeyboardButton
import constants

def Btn(text, **kwargs):
    return InlineKeyboardButton(text, **kwargs)

def ConnectVK():
    return Btn("🔑 Подключить ВК", url=constants.VK_AUTH_URL)

