from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuUzbek=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍽 Menyu"),
        ],
        [
            KeyboardButton(text="ℹ️ Ma'lumot"),
            KeyboardButton(text="📞  Aloqa"),
        ],
        # [
        #     KeyboardButton(text="📍 Manzil"),
        # ],
        [
            KeyboardButton(text="✍️ Fikr bildirish"),
            KeyboardButton(text="⚙️ Sozlamalar"),
        ],
    ],
    resize_keyboard=True
)