from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

dostafkaMenu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💵 Yetib kelganda naqd to'lash")
        ],
        [
            KeyboardButton(text="💳  Click"),
            KeyboardButton(text="💳  Payme"),
        ],
        [
            KeyboardButton(text="↩️ Ortga  qaytish"),
        ],
    ],
    resize_keyboard=True
)