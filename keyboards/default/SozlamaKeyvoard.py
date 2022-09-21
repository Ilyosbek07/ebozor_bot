from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="🌐  Tilni  almashtirish"
                                                    )
                                   ],
                                   [
                                       KeyboardButton(text="🔙 Ortga qaytish"),
                                   ],
                               ])