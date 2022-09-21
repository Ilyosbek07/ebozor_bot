from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


spriteMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sprite 0,5 lt", callback_data="sprite2"),
            InlineKeyboardButton(text="Sprite 1 lt", callback_data="sprite3"),
        ],
        [
            InlineKeyboardButton(text="Sprite 1,5 lt", callback_data="sprite4"),
            InlineKeyboardButton(text="Sprite can", callback_data="sprite5"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)