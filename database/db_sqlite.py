import sqlite3 as sq


class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()

    def sql_get_timetable_today(self, date):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM timetable WHERE date = ? """, (date,)).fetchall()

    def get_all(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM timetable;",).fetchone()

# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO menu VALUES '
#                     '(?, ?, ?, ?)', tuple(data.values()))
#         base.commit()
