import db.vk_auth
import db.vk_status
import time
import globals
import utils
from telegram.bot import Bot
from telegram.utils.request import Request
from telegram import InputMediaPhoto

request = Request(proxy_url='https://118.99.95.136:8080')
bot = Bot(utils.get_bot_token(), request=request)


def send_post(user_id, post):
    photos = []
    audios = []

    for item in post['attachments']:
        if item['type'] == 'photo':
            photos.append(item['photo']['sizes'][-1]['url'])
        # elif item['type'] == 'audio':
        #     audios.append({
        #         audio=
        #     })

    bot.send_message(user_id, f'<a href="https://vk.com/wall{post["source_id"]}_{post["post_id"]}">Новый пост!</a>\n', parse_mode='HTML', disable_web_page_preview=True)

    if len(photos) > 1:
        input_media_photos = [InputMediaPhoto(media=url) for url in photos]
        bot.send_media_group(user_id, media=input_media_photos)
        bot.send_message(user_id, post['text'])
    elif len(photos) == 1:
        bot.send_photo(user_id, photo=photos[0], caption=post['text'])
    else:
        bot.send_message(user_id, post['text'])


def main():
    while True:
        try:
            all_vk_users = db.vk_auth.get_all()
            for vk_user in all_vk_users:
                user_id, vk_id, access_token = vk_user
                print(user_id, vk_id, access_token)
                last_post_ts = db.vk_status.get_last_post_ts(user_id)
                if not last_post_ts:
                    last_post_ts = int(time.time())

                feed = globals.vk.get_newsfeed('post', access_token=access_token, count=5)
                for post in feed['items']:
                    if post['date'] > last_post_ts:
                        send_post(user_id, post)
                        last_post_ts = post['date']

                db.vk_status.set_last_post_ts(user_id, last_post_ts)

            time.sleep(1)
        except:
            pass


if __name__ == '__main__':
    main()