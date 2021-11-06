from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇺🇿UZ🇺🇿'),
            KeyboardButton(text='🇷🇺RU🇷🇺'),
        ],
    ],
    resize_keyboard=True
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱Contact ulashish', request_contact=True),
        ],
    ],
    resize_keyboard=True
)
