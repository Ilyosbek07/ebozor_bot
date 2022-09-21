from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbek"),
        ],
        [
            KeyboardButton(text="🇷🇺 Rus"),
            KeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English"),
        ]
    ],
    resize_keyboard=True
)