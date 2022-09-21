from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul
ichimliklarMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Coca-cola", callback_data="cocacolaa"),
            InlineKeyboardButton(text="Pepsi", callback_data="pepsi0"),
            InlineKeyboardButton(text="Fanta", callback_data="fanta0"),
            InlineKeyboardButton(text="Soklar", callback_data="soklar1"),
        ],
        [
            InlineKeyboardButton(text="Adrenaline", callback_data="adrenaline1"),
            InlineKeyboardButton(text="Flash", callback_data="flash1"),
        ],
        [
            InlineKeyboardButton(text="Chortoq", callback_data="chortoq1"),
            InlineKeyboardButton(text="Nistle", callback_data="nistle1"),
            InlineKeyboardButton(text="Sprite", callback_data="sprite1"),
            InlineKeyboardButton(text="Familiy", callback_data="familiy1")
        ],
        [
            InlineKeyboardButton(text="Choy", callback_data="choy1"),
            InlineKeyboardButton(text="Kofe", callback_data="kofe1"),
        ],
    ],
    resize_keyboard=True
)

