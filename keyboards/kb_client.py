from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_1 = KeyboardButton('/Расписание_на_сегодня')
button_2 = KeyboardButton('/Расписание_на_завтра')
button_3 = KeyboardButton('/Все_расписание')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button_1).insert(button_2).add(button_3)
