from aiogram import types
import database
from imports import dp
from keyboards import kb_client
import datetime as dt


async def start(message: types.Message):
    await message.answer("Привет!\n\nЯ бот для студентов группы 01-ЭКЗ2831 "
                         "АТиСО.\n\nДля продолжения выбери категорию",
                         reply_markup=kb_client)


async def get_timetable_for_today(message: types.Message):
    today = dt.date.today().strftime('%d/%m')
    result = database.db_sqlite.Database('database/db.db').\
        sql_get_timetable_by_date(today)
    res = ''
    for i in result:
        row = ' | '.join(i[1:])
        res += f'\n\n{row}'
    await message.answer(res)


async def get_timetable_for_tomorrow(message: types.Message):
    tomorrow = (dt.date.today() + dt.timedelta(days=1)).strftime('%d/%m')
    result = database.db_sqlite.Database('database/db.db').\
        sql_get_timetable_by_date(tomorrow)
    if result == []:
        await message.answer("Пар на завтра нет. Скорее всего завтра воскресенье.")
    else:
        res = ''
        for i in result:
            row = ' | '.join(i[1:])
            res += f'\n\n{row}'
        await message.answer(res)


async def get_all_timetable(message: types.Message):
    result = database.db_sqlite.Database('database/db.db').sql_get_all()
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
    await message.reply(f"Расписание на сессию 1 часть:\n{res_1}")
    await message.reply(f"Расписание на сессию 2 часть:\n{res_2}")


def register_handlers_for_client():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(get_timetable_for_today, commands=['Расписание_на_сегодня'])
    dp.register_message_handler(get_timetable_for_tomorrow, commands=['Расписание_на_завтра'])
    dp.register_message_handler(get_all_timetable, commands=['Все_расписание'])
