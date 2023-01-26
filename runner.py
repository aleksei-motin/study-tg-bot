# -*- coding: utf8 -*-

import handlers
from imports import executor, dp, t


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
