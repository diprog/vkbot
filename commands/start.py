from interface import menus
import db.vk_auth
import globals
command = 'start'


def action(update, context):
    try:
        access_token, vk_id = update.message.text.split(' ')[1].split(',')
        vk_user = globals.vk.get_user(vk_id, access_token=access_token)
        db.vk_auth.add(update.message.from_user.id, vk_id, access_token)
        update.message.reply_text(f'Добро пожаловать, {vk_user["first_name"]}!\nТеперь я буду отправлять тебе твою ленту.')

    except IndexError:
        update.message.reply_text(
            #'Привет!\nЯ могу транслировать твою ленту ВК в наш с тобой чат или желаемый канал/группу.\nДля начала нужно подключить свой аккаунт ВК.',
            'Привет!\nЯ могу транслировать твою ленту ВК в наш с тобой чат.\nДля начала нужно подключить свой аккаунт ВК.',
            reply_markup=menus.Start())

