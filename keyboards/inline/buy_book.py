from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

book_keys = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="📍 Eng yaqin manzilni topish", callback_data="mylocation"),
        InlineKeyboardButton(text="📲  Kontaktimni ulashish", callback_data="mycontact"),
    ],
])