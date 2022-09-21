from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul
pitsaMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Margarita", callback_data="pitsa1"),
            InlineKeyboardButton(text="Gribnaya", callback_data="pitsa2"),
            InlineKeyboardButton(text="Ovoshnoy", callback_data="pitsa3"),
        ],
        [
            InlineKeyboardButton(text="Halol Pitsa", callback_data="pitsa4"),
            InlineKeyboardButton(text="Kurinnaya Grudinka", callback_data="pitsa5"),
        ],
        [

            InlineKeyboardButton(text="Pepperoni", callback_data="pitsa6"),
            InlineKeyboardButton(text="Meksikano", callback_data="pitsa7"),
            InlineKeyboardButton(text="Drakon", callback_data="pitsa8"),
        ],
        [
            InlineKeyboardButton(text="Vetchina S Gribami", callback_data="pitsa9"),
            InlineKeyboardButton(text="Barbekyu", callback_data="pitsa10"),
        ],
        [
            InlineKeyboardButton(text="Firmennaya", callback_data="pitsa11"),
            InlineKeyboardButton(text="Myasnaya", callback_data="pitsa12"),
            InlineKeyboardButton(text="4-Myaso", callback_data="pitsa13"),
        ],
        [
            InlineKeyboardButton(text="Americano", callback_data="pitsa14"),
            InlineKeyboardButton(text="Super Assorti", callback_data="pitsa15"),
        ],
        [
            InlineKeyboardButton(text="Miks", callback_data="pitsa16"),
            InlineKeyboardButton(text="Don Karleone", callback_data="pitsa17"),
            InlineKeyboardButton(text="Mafia", callback_data="pitsa18"),
        ],
    ],
    resize_keyboard=True
)