from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard(*args):
    keyboard = ReplyKeyboardMarkup()

    for name_button in args:
        keyboard.add(KeyboardButton(name_button))

    return keyboard
