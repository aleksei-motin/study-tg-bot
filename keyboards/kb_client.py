from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_1 = KeyboardButton('/Расписание')
# button_2 = KeyboardButton('/Лекции')
# button_3 = KeyboardButton('/Ответы')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button_1)  # .insert(button_2).insert(button_3)
