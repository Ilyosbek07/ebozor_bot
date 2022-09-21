from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


categoryMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Lavash obichniy", callback_data="lavashshsh"),
            InlineKeyboardButton(text="Lavash Pishloqli", callback_data="lavashpishloq"),
        ],
        [
        InlineKeyboardButton(text="BIG Lavash", callback_data="lavashbig"),
        ],
        [
            InlineKeyboardButton(text="Tandir Lavash", callback_data="lavashtandir"),
            InlineKeyboardButton(text="BIG Tandir Lavash", callback_data="lavashbigtandir"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)
