# -*- coding: utf8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


timetable = InlineKeyboardMarkup(row_width=2)
timetable_today_button = InlineKeyboardButton(text='Расписание на сегодня', callback_data='timetable_today')
timetable_tomorrow_button = InlineKeyboardButton(text='Расписание на завтра', callback_data='timetable_tomorrow')
timetable_exams_button = InlineKeyboardButton(text='Аттестация', callback_data='timetable_exams')
timetable_all_button = InlineKeyboardButton(text='Все расписание', callback_data='timetable_all')
timetable_from_atiso_button = InlineKeyboardButton(text='Расписание на сайте', callback_data='timetable_site')
timetable_excel_button = InlineKeyboardButton(text='Расписание с заданиями в Excel', callback_data='timetable_excel')

timetable\
    .add(timetable_today_button).insert(timetable_tomorrow_button)\
    .add(timetable_exams_button).insert(timetable_excel_button)\
    .add(timetable_all_button).insert(timetable_from_atiso_button)
