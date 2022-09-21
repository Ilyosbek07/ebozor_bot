from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import  lavpish_callback, lavbig_callback

# 1-usul
nonDogMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Non Dog  13000", callback_data="nondog"),
            InlineKeyboardButton(text="Non Burger  23000", callback_data="nonburger"),
        ],
    ],
    resize_keyboard=True
)

# # Pitta obichniy uchun Keyboard
# dognonMenu=InlineKeyboardMarkup(row_width=2)
# pish=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavpish_callback.new(item_name="pish"))
# dognonMenu.insert(pish)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# dognonMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# dognonMenu.insert(back_button)
#
# # Big Pitta uchun keyboard
# nonburgerMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# nonburgerMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# nonburgerMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# nonburgerMenu.insert(back_button)



