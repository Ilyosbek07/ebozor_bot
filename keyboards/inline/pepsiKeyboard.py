from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


pepsiMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Pepsi 0,5 lt", callback_data="pepsi5"),
            InlineKeyboardButton(text="Pepsi 1 lt", callback_data="pepsi2"),
        ],
        [
            InlineKeyboardButton(text="Pepsi 1,5 lt", callback_data="pepsi3"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)