from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


sokMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bliss", callback_data="bliss1"),
            InlineKeyboardButton(text="Dena", callback_data="dena1"),
        ],
        [
            InlineKeyboardButton(text="Rich", callback_data="rich1"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)