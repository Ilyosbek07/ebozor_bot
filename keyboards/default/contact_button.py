from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📲 Raqamimni yuborish",
                                                      request_contact=True)
                                   ],
                                   [
                                       KeyboardButton(text="🔙 Ortga qaytish"),
                                   ],
                               ])