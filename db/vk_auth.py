from db import ConnectionCursor


def add(user_id, vk_id, access_token):
    with ConnectionCursor() as c:
        c.execute('DELETE FROM vk_auth WHERE user_id=?', (user_id,))
        c.execute('INSERT INTO vk_auth VALUES (?,?,?)', (user_id, vk_id, access_token))


def remove(user_id):
    with ConnectionCursor() as c:
        c.execute('DELETE FROM vk_auth WHERE user_id=?', (user_id,))


def get_all():
    with ConnectionCursor(commit=False) as c:
        c.execute('SELECT * FROM vk_auth')
        return c.fetchall()