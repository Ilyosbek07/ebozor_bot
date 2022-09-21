from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

joylashuvMenu = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📍  Joylashuvimni yuborish",
                                                      request_location=True)
                                   ],
                                   [
                                       KeyboardButton(text="🔙 Ortga qaytish"),
                                   ],
                               ])
