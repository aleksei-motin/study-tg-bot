from aiogram.utils import executor

from database import db_sqlite
from handlers import h_client, h_admin
from imports import dp


async def on_startup(_):
    print("Бот запустился.")

h_client.register_handlers_for_client()
# h_admin.register_handlers_for_admin()


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    main()
