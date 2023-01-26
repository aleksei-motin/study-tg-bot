# -*- coding: utf8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


timetable = InlineKeyboardMarkup(row_width=2)
timetable_today_button = InlineKeyboardButton(text='Сегодня', callback_data='timetable_today')
timetable_tomorrow_button = InlineKeyboardButton(text='Завтра', callback_data='timetable_tomorrow')
timetable_exams_button = InlineKeyboardButton(text='Аттестация', callback_data='timetable_exams')
timetable_all_button = InlineKeyboardButton(text='Все расписание', callback_data='timetable_all')
timetable_from_atiso_button = InlineKeyboardButton(text='На сайте вуза', url='https://atiso.ru/students/rasp/?'
                                                                                   'arFilter_239=2722427323&arFilter_'
                                                                                   '246=&arFilter_247=&arFilter_308_'
                                                                                   'MIN=&arFilter_308_MAX=&set_filter='
                                                                                   '%CF%EE%EA%E0%E7%E0%F2%FC')
timetable_excel_button = InlineKeyboardButton(text='Excel от Настасьи', url='https://docs.google.com/'
                                                                                         'spreadsheets/d/12BoPzN6ffi_'
                                                                                         'DBVmFjcBCvN9OknmIZGHUxFXj_d-'
                                                                                         'Z_0w/edit#gid=0')

timetable\
    .add(timetable_today_button).insert(timetable_tomorrow_button)\
    .add(timetable_exams_button).insert(timetable_all_button)\
    .add(timetable_excel_button).insert(timetable_from_atiso_button)
