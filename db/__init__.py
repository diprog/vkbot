import sqlite3

class ConnectionCursor():
    def __init__(self, commit=True):
        self.connection = None
        self.commit = commit

    def __enter__(self):
        self.connection = sqlite3.connect('db.db')
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, type, value, traceback):
        if self.commit:
            self.connection.commit()
        self.connection.close()


with ConnectionCursor() as c:
    try:
        # Таблица vk_auth. Хранит ключи доступа пользователей.
        c.execute('''CREATE TABLE vk_auth
                     (
                     [user_id] UNSIGNED BIG INT PRIMARY KEY,
                     [vk_id] INTEGER,
                     [access_token] TEXT
                     )''')

        # Таблица vk_status. Нужна для получения новых постов из ВК.
        c.execute('''CREATE TABLE vk_status
                             (
                             [user_id] UNSIGNED BIG INT PRIMARY KEY,
                             [last_post_ts] REAL
                             )''')
    except sqlite3.OperationalError:
        pass

