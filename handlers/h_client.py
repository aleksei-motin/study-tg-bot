from aiogram import types

from imports import dp
from keyboards import kb_client


async def start(message: types.Message):
    await message.answer("Выбери категорию", reply_markup=kb_client)


async def get_timetable(message: types.Message):
    await message.answer(f"Расписание на сегодня: \nляляля\nтутуту\nкококо")


def register_handlers_for_clients():
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(get_timetable, commands=['Расписание'])
