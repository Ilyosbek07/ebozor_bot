from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menyularKeyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒 Savat"),
        ],
        [
            KeyboardButton(text="🌯️ Lavash"),
            KeyboardButton(text="🍔  Burger"),
        ],
        [
            KeyboardButton(text="🍕 Pitsa"),
        ],
        [
            KeyboardButton(text="🌮️ Donar"),
            KeyboardButton(text="🌭 Hot-Dog"),
        ],
        [
            KeyboardButton(text="🥙 Pitta"),
        ],
        [
            KeyboardButton(text="🧆 Myaso"),
            KeyboardButton(text="🥙 Non-Dog"),
        ],
        [
            KeyboardButton(text="🍟 FRI"),
        ],
        [
            KeyboardButton(text="🥤 Ichimliklar"),
            KeyboardButton(text="🍰 Shirinliklar"),
        ],
        [
            KeyboardButton(text="🔙 Ortga qaytish"),
        ],
    ],
    resize_keyboard=True
)