from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


choyMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'k  Choy", callback_data="kokchoy"),
            InlineKeyboardButton(text="Qora  Choy", callback_data="qorachoy"),
        ],
        [
            InlineKeyboardButton(text="Limon  Choy", callback_data="limonchoy"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)