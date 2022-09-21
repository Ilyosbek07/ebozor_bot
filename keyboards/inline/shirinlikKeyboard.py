from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import  lavpish_callback, lavbig_callback

# 1-usul
shirinlikMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Banana  13000", callback_data="banana"),
            InlineKeyboardButton(text="Maxroviy  13000", callback_data="maxroviy"),
        ],
[
            InlineKeyboardButton(text="Shokoladniy  13000", callback_data="shokoladniy"),
        ],
        [
            InlineKeyboardButton(text="Piramida  13000", callback_data="piramida"),
            InlineKeyboardButton(text="Lakomka  13000", callback_data="lakomka"),
        ],
    ],
    resize_keyboard=True
)

# # Banana uchun Keyboard
# bananaMenu=InlineKeyboardMarkup(row_width=2)
# pish=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavpish_callback.new(item_name="pish"))
# bananaMenu.insert(pish)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# bananaMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# bananaMenu.insert(back_button)
#
# # Maxroviy keyboard
# maxroviyMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# maxroviyMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# maxroviyMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# maxroviyMenu.insert(back_button)
#
#
# # Shokoladniy uchun keyboard
# shokoladniyMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# shokoladniyMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# shokoladniyMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# shokoladniyMenu.insert(back_button)
#
# # Piramida uchun keyboard
# piramidaMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# piramidaMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# piramidaMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# piramidaMenu.insert(back_button)
#
# # Lakomka uchun keyboard
# lakomkaMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# lakomkaMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# lakomkaMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# lakomkaMenu.insert(back_button)