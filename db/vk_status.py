from db import ConnectionCursor


def set_last_post_ts(user_id, post_date):
    with ConnectionCursor() as c:
        c.execute('DELETE FROM vk_status WHERE user_id=?', (user_id,))
        c.execute('INSERT INTO vk_status VALUES (?,?)', (user_id, post_date))


def get_last_post_ts(user_id):
    with ConnectionCursor() as c:
        c.execute('SELECT * FROM vk_status WHERE user_id=?', (user_id,))
        row = c.fetchone()
        if row:
            return row[1]