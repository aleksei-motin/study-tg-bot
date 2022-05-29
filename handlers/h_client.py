from aiogram import types
from datetime import date
import database
from imports import dp
from keyboards import kb_client


async def start(message: types.Message):
    await message.answer("Привет!\n\nЯ бот для студентов группы 01-ЭКЗ2831 "
                         "АТиСО.\n\nДля продолжения выбери категорию",
                         reply_markup=kb_client)


async def get_timetable(message: types.Message):
    await message.answer(database.db_sqlite.Database('database/db.db').get_all())


def register_handlers_for_client():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(get_timetable, commands=['Расписание'])
