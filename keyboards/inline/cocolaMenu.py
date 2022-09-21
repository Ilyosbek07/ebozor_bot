from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


CocacolaMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Coca-cola 0,5 lt", callback_data="coca"),
            InlineKeyboardButton(text="Coca-cola 1 lt", callback_data="cocal"),
        ],
        [
            InlineKeyboardButton(text="Coca-cola 1,5 lt", callback_data="cocala"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)