# -*- coding: utf8 -*-

import time as t

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

import handlers
from api_token import API_TOKEN


storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)


async def on_startup(_):
    handlers.Handlers().get_timetable()

    print("Бот запустился.")


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            t.sleep(15)
