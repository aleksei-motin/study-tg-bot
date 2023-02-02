# -*- coding: utf8 -*-

import datetime as dt
import time

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

import db
import keyboard
from api_token import API_TOKEN


storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)


def add_user_by_use(user_id, username):
    if not db.Database('db.db').sql_user_exists(user_id):
        db.Database('db.db').sql_add_user(user_id, username)


def update_last_use(user_id):
    timestamp_now = str(dt.datetime.now())
    db.Database('db.db').sql_update_last_active(timestamp_now, user_id)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    add_user_by_use(message.from_user.id, message.from_user.username)
    update_last_use(message.from_user.id)
    await message.answer("Привет!\n\nЯ бот c расписанием занятий."
                         "\nДля продолжения выбери вариант расписания."
                         "\n\n!!! Если использовал прежнюю версию бота, "
                         "то удали чат и запусти заново для устранения проблем отображения !!!",
                         reply_markup=keyboard.timetable)


@dp.message_handler(commands='usage')
async def users_usage(message: types.Message):
    users_usage_db_result = db.Database('db.db').sql_users_usage()
    if message.from_user.id == 427632571:
        users_usage_db_result_formatted = ''
        for i in users_usage_db_result:
            row = ' | '.join(map(str, i))
            users_usage_db_result_formatted += f'\n\n{row}'
        await message.answer(users_usage_db_result_formatted)
    else:
        await message.answer("Доступ запрещен")


@dp.callback_query_handler(text='timetable_today')
async def get_timetable_today(callback: types.CallbackQuery):
    add_user_by_use(callback.from_user.id, callback.from_user.username)
    update_last_use(callback.from_user.id)
    sql_result = db.Database('db.db').sql_get_timetable_by_date(dt.date.today().strftime('%d/%m'))
    result = ''
    if not sql_result:
        await callback.message.answer('Сегодня занятий нет')
    else:
        for i in sql_result:
            row = ' | '.join(map(str, i))
            result += f'\n\n{row}'
        await callback.message.answer(f'Занятия на сегодня{result}', reply_markup=keyboard.timetable)


@dp.callback_query_handler(text='timetable_tomorrow')
async def get_timetable_tomorrow(callback: types.CallbackQuery):
    add_user_by_use(callback.from_user.id, callback.from_user.username)
    update_last_use(callback.from_user.id)
    sql_result = db.Database('db.db').sql_get_timetable_by_date((dt.date.today() + dt.timedelta(days=1)).strftime('%d/%m'))
    result = ''
    if not sql_result:
        await callback.message.answer('Завтра занятий нет')
    else:
        for i in sql_result:
            row = ' | '.join(map(str, i))
            result += f'\n\n{row}'
        await callback.message.answer(f'Занятия на завтра{result}', reply_markup=keyboard.timetable)


@dp.callback_query_handler(text='timetable_exams')
async def get_timetable_exams(callback: types.CallbackQuery):
    add_user_by_use(callback.from_user.id, callback.from_user.username)
    update_last_use(callback.from_user.id)
    sql_result = db.Database('db.db').sql_get_exams('З', 'КЭ, Э', 'КЭ, КР(П), Э', 'НИР', 'НИР, З', 'П', 'П, З')
    result = ''
    for i in sql_result:
        row = ' | '.join(map(str, i))
        result += f'\n\n{row}'
    await callback.message.answer(f'Все зачеты, консультации, экзамены, защиты{result}', reply_markup=keyboard.timetable)


@dp.callback_query_handler(text='timetable_all')
async def get_timetable_all(callback: types.CallbackQuery):
    add_user_by_use(callback.from_user.id, callback.from_user.username)
    update_last_use(callback.from_user.id)
    sql_result = db.Database('db.db').sql_get_all_lessons()
    long = len(sql_result)
    half = int(long / 2)
    part_1 = sql_result[:half]
    result_1 = ''
    for i in part_1:
        row = ' | '.join(map(str, i))
        result_1 += f'\n\n{row}'
    part_2 = sql_result[half:]
    result_2 = ''
    for i in part_2:
        row = ' | '.join(map(str, i))
        result_2 += f'\n\n{row}'
    await bot.send_message(callback.from_user.id, f'Расписание на сессию 1 часть{result_1}')
    await callback.message.answer(f'Расписание на сессию 1 часть{result_2}', reply_markup=keyboard.timetable)


async def on_startup(_):
    print("Бот запустился.")


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            time.sleep(15)
