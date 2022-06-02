from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_1 = KeyboardButton('/Расписание_на_сегодня')
button_2 = KeyboardButton('/Все_расписание')
# button_3 = KeyboardButton('/Ответы')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button_1).add(button_2)#.insert(button_3)
