from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


familyMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Family  0,5 lt", callback_data="family2"),
            InlineKeyboardButton(text="Family   1 lt", callback_data="family3"),
        ],
        [
            InlineKeyboardButton(text="Family   1,5 lt", callback_data="family4"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)