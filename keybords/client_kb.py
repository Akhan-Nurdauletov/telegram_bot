from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('Режим работы')
b2 = KeyboardButton('Расположение')
b3 = KeyboardButton('Меню')
b4 = KeyboardButton('Контакты')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton ('Отправить где Я', request_location=True)

kb_client=ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b3).row(b1, b2).add(b4)
