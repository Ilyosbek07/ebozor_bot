from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import  lavpish_callback, lavbig_callback

# 1-usul
pittaMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Pitta obichniy", callback_data="pitta"),
            InlineKeyboardButton(text="BIG Pitta", callback_data="bigpitta"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)