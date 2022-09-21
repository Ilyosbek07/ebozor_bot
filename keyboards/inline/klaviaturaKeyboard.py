from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


klaviaturaMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tanlangan:", callback_data="tanladi"),
        ],
        [
            InlineKeyboardButton(text="1", callback_data="one"),
            InlineKeyboardButton(text="2", callback_data="two"),
            InlineKeyboardButton(text="3", callback_data="three"),
        ],
        [
            InlineKeyboardButton(text="4", callback_data="four"),
            InlineKeyboardButton(text="5", callback_data="five"),
            InlineKeyboardButton(text="6", callback_data="six"),
        ],
        [
            InlineKeyboardButton(text="7", callback_data="seven"),
            InlineKeyboardButton(text="8", callback_data="eight"),
            InlineKeyboardButton(text="9", callback_data="nine"),
        ],
        [
            InlineKeyboardButton(text="0", callback_data="zero"),
            InlineKeyboardButton(text="🗑 O'chirish", callback_data="delete"),
        ],
        [
            InlineKeyboardButton(text="🛒 Savatga joylash", callback_data="basket"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)