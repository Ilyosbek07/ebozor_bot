from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


fantaMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Fanta 0,5 lt", callback_data="fanta5"),
            InlineKeyboardButton(text="Fanta 1 lt", callback_data="fanta2"),
        ],
        [
            InlineKeyboardButton(text="Fanta 1,5 lt", callback_data="fanta3"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)