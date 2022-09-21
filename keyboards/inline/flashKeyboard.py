from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


flashMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="FLASH  KATTA", callback_data="flashbig"),
            InlineKeyboardButton(text="FLASH  KICHIK", callback_data="flashmini"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)