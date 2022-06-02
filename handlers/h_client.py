from aiogram import types
from datetime import date
import database
from imports import dp
from keyboards import kb_client
import datetime as dt


async def start(message: types.Message):
    await message.answer("Привет!\n\nЯ бот для студентов группы 01-ЭКЗ2831 "
                         "АТиСО.\n\nДля продолжения выбери категорию",
                         reply_markup=kb_client)


async def get_timetable_today(message: types.Message):
    today = dt.date.today().strftime('%d/%m')
    result = database.db_sqlite.Database('database/db.db').sql_get_timetable_by_date(today)
    print(result)
    res = ''
    for i in result:
        row = ' | '.join(i[1:])
        res += f'\n\n{row}'
    await message.answer(res)


async def get_all_timetable(message: types.Message):
    result = database.db_sqlite.Database('database/db.db').sql_get_all()
    await message.reply(f"Расписание на сессию:\n{result}")

def register_handlers_for_client():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(get_timetable_today, commands=['Расписание_на_сегодня'])
    dp.register_message_handler(get_all_timetable, commands=['Все_расписание'])
