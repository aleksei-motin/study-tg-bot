import time

from aiogram.utils import executor

from handlers import h_client
from imports import dp


async def on_startup(_):
    print("Бот запустился.")

h_client.register_handlers_for_client()


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            time.sleep(15)
