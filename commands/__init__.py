from . import *
import os
from importlib import import_module
from telegram.ext import CommandHandler

commands = list()

dirpath = os.path.dirname(__file__)
for path in os.listdir(dirpath):
    # Тянем все файлы, кроме __init__.py
    if not path.startswith('__'):
        imported_module = import_module('.' + path[:-3], package=__name__)
        command_text = getattr(imported_module, 'command')
        func = getattr(imported_module, 'action')
        commands.append(CommandHandler(command_text, func))

