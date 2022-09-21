from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import  lavpish_callback, lavbig_callback

# 1-usul
hotdogMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Hot-Dog obichniy", callback_data="hotdog"),
            InlineKeyboardButton(text="Chis Dog", callback_data="chisdog"),
        ],
        [
            InlineKeyboardButton(text="Korolevskiy", callback_data="korolevskiy"),
            InlineKeyboardButton(text="Hot-Dog Myasnoy", callback_data="hotdogmyasnoy"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)

# # Hot-Dog obichniy uchun Keyboard
# doghotMenu=InlineKeyboardMarkup(row_width=2)
# pish=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavpish_callback.new(item_name="pish"))
# doghotMenu.insert(pish)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# doghotMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# doghotMenu.insert(back_button)
#
# # Chis Dog uchun keyboard
# chisdogMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# chisdogMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# chisdogMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# chisdogMenu.insert(back_button)
#
#
# # Korolevskiy uchun keyboard
# korolevskiyMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# korolevskiyMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# korolevskiyMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# korolevskiyMenu.insert(back_button)
#
# # Hot Dog myasnoy uchun keyboard
# hotdogmyasnoyMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# hotdogmyasnoyMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# hotdogmyasnoyMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# hotdogmyasnoyMenu.insert(back_button)