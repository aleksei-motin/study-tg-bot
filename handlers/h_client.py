# -*- coding: utf8 -*-
from aiogram import types
import database
from imports import dp
from keyboards import kb_client
import datetime as dt


def add_user_by_use(message: types.Message):
    if not database.db_sqlite.Database('database/db.db').sql_user_exists(
            message.from_user.id):
        database.db_sqlite.Database('database/db.db').sql_add_user(
            message.from_user.id, message.from_user.username)


def update_last_use(message: types.Message):
    timestamp = str(dt.datetime.now())
    user_id = message.from_user.id
    database.db_sqlite.Database('database/db.db').\
        sql_update_last_active(timestamp, user_id)


async def start(message: types.Message):
    add_user_by_use(message)
    update_last_use(message)
    await message.answer("Привет!\n\nЯ бот c расписанием занятий."
                         "\nДля продолжения выбери вариант расписания.",
                         reply_markup=kb_client)


async def get_timetable_for_today(message: types.Message):
    add_user_by_use(message)
    update_last_use(message)
    today = dt.date.today().strftime('%d/%m')
    result = database.db_sqlite.Database('database/db.db'). \
        sql_get_timetable_by_date(today)
    if result == []:
        await message.reply(
            "Сегодня занятий нет.",
            reply_markup=kb_client)
    else:
        res = ''
        for i in result:
            row = ' | '.join(i[1:])
            res += f'\n\n{row}'
        await message.reply(res, reply_markup=kb_client)


async def get_timetable_for_tomorrow(message: types.Message):
    add_user_by_use(message)
    update_last_use(message)
    tomorrow = (dt.date.today() + dt.timedelta(days=1)).strftime('%d/%m')
    result = database.db_sqlite.Database('database/db.db'). \
        sql_get_timetable_by_date(tomorrow)
    if result == []:
        await message.reply(
            "Завтра занятий нет.",
            reply_markup=kb_client)
    else:
        res = ''
        for i in result:
            row = ' | '.join(i[1:])
            res += f'\n\n{row}'
        await message.answer(res, reply_markup=kb_client)


async def get_exams(message: types.Message):
    result = database.db_sqlite.Database('database/db.db').\
        sql_get_exams('З', 'КЭ, Э')
    res = ''
    for i in result:
        row = ' | '.join(i)
        res += f'\n\n{row}'
    await message.reply(res, reply_markup=kb_client)


async def get_all_timetable(message: types.Message):
    add_user_by_use(message)
    update_last_use(message)
    result = database.db_sqlite.Database('database/db.db').\
        sql_get_all_lessons()
    long = len(result)
    half = int(long / 2)
    part_1 = result[:half]
    res_1 = ''
    for i in part_1:
        row = ' | '.join(i)
        res_1 += f'\n\n{row}'
    part_2 = result[half:]
    res_2 = ''
    for i in part_2:
        row = ' | '.join(i)
        res_2 += f'\n\n{row}'
    await message.reply(f"Расписание на сессию 1 часть:\n{res_1}",
                        reply_markup=kb_client)
    await message.reply(f"Расписание на сессию 2 часть:\n{res_2}",
                        reply_markup=kb_client)


def register_handlers_for_client():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(get_timetable_for_today,
                                commands=['Расписание_на_сегодня'])
    dp.register_message_handler(get_timetable_for_tomorrow,
                                commands=['Расписание_на_завтра'])
    dp.register_message_handler(get_exams, commands=['Зачеты_и_экзамены'])
    dp.register_message_handler(get_all_timetable, commands=['Все_расписание'])
