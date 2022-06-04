# -*- coding: utf8 -*-
import sqlite3 as sq


class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()

    def sql_user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("""SELECT * FROM users WHERE 
            user_id = ?""", (user_id,)).fetchmany(1)
            return bool(len(result))

    def sql_add_user(self, user_id, username):
        with self.connection:
            return self.cursor.execute("""INSERT INTO users (user_id, username) 
            VALUES (?, ?)""", (user_id, username,))

    def sql_update_last_active(self, last_use, user_id):
        with self.connection:
            return self.cursor.execute("""UPDATE users SET 
            last_active = ? WHERE user_id = ?""", (last_use, user_id,))

    def sql_get_user(self, user_id):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM users WHERE 
            user_id = ?""", (user_id,))

    def sql_get_timetable_by_date(self, date):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM timetable WHERE 
            date = ?""", (date,)).fetchall()

    def sql_get_exams(self, type_1, type_2):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM timetable WHERE
            type = ? OR type = ?""", (type_1, type_2)).fetchall()


    def sql_get_all_lessons(self):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM timetable""",).\
                fetchall()
