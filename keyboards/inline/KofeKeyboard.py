from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


kofeMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="MacCoffe", callback_data="maccoffe"),
            InlineKeyboardButton(text="NesCafe GOLD", callback_data="nescafegold"),
        ],
        [
            InlineKeyboardButton(text="NesCafe Classic", callback_data="nescafeclassic"),
            InlineKeyboardButton(text="JACOBS", callback_data="jacobs"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)