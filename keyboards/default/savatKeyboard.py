from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

savatMenu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Buyurtmani tasdiqlash"),
            KeyboardButton(text="📞 Qo'ng'iroq qilish")
        ],
        [
            KeyboardButton(text="🗒 Yana buyurtma tanlash"),
            KeyboardButton(text="🔝 Asosiy menyu")
        ],
        [
            KeyboardButton(text="🔙  Ortga qaytish"),
        ],
    ],
    resize_keyboard=True
)

# To'lov qilish usuli
tulovMenu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚗  Yetkazib  berish"),
            KeyboardButton(text="🚶  Olib  ketish"),
        ],
    ],
    resize_keyboard=True
)