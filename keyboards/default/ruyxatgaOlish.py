from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ruyxat = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📱 Kontaktimni yuborish",
                                                      request_contact=True)
                                   ],
                                   [
                                       KeyboardButton(text="🔙 Ortga qaytish"),
                                   ],
                               ])