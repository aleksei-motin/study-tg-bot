# -*- coding: utf8 -*-

import sqlite3


class Database:
    def __init__(self, db_file='db.db'):
        self.connection = sqlite3.connect(db_file)
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

    def sql_users_usage(self):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM users""",).fetchall()

    def sql_get_timetable_by_date(self, date):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM timetable WHERE 
            date = ?""", (date,)).fetchall()

    def sql_get_exams(self, type_1, type_2, type_3, type_4, type_5, type_6, type_7):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM timetable WHERE
            type = ? OR 
            type = ? OR 
            type = ? OR 
            type = ? OR 
            type = ? OR 
            type = ? OR
            type = ?""", (type_1, type_2, type_3, type_4, type_5, type_6, type_7)).fetchall()

    def sql_get_all_lessons(self):
        with self.connection:
            return self.cursor.execute("""SELECT * FROM timetable""",).fetchall()
