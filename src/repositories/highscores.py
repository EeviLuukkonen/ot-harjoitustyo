import sqlite3

class Highscore():
    def __init__(self, connection):
        self._connection = connection

    def create(self, time, level):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into highscores (time, level) values (?, ?)',
            (time,level)
        )

        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute('select * from highscores order by time limit 5')

        rows = cursor.fetchall()

        return rows
