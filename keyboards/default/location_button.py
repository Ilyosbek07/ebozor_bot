from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📍  Manzilimni yuborish",
                                                      request_location=True)
                                   ],
                                   [
                                       KeyboardButton(text="🔙 Ortga qaytish"),
                                   ],
                               ])
