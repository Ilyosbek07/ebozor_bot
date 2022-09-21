from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


nistleMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Nistle 0,5 lt", callback_data="nistle2"),
            InlineKeyboardButton(text="Nistle 1 lt", callback_data="nistle3"),
        ],
        [
            InlineKeyboardButton(text="Nistle 1,5 lt", callback_data="nistle4"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)