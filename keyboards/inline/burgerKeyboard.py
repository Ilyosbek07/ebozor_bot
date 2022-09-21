from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul
burgerMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Gamburger", callback_data="gamburg"),
            InlineKeyboardButton(text="Cheeseburger", callback_data="cheeseburg"),
        ],
        [
        InlineKeyboardButton(text="Halol Burger", callback_data="burgerhalol"),
        ],
        [
            InlineKeyboardButton(text="BIG Burger", callback_data="bigburger"),
            InlineKeyboardButton(text="BIG Cheeseburger", callback_data="bigcheeseburger"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel"),
        ],
    ],
    resize_keyboard=True
)

# # Gamburger uchun keyboard
# gamburMenu=InlineKeyboardMarkup(row_width=2)
# gamburg=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=gambur_callback.new(item_name="gamburgerer"))
# gamburMenu.insert(gamburg)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# gamburMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# gamburMenu.insert(back_button)
#
# # Cheeseburger uchun Keyboard
# cheeseburgMenu=InlineKeyboardMarkup(row_width=2)
# pish=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavpish_callback.new(item_name="pish"))
# cheeseburgMenu.insert(pish)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# cheeseburgMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# cheeseburgMenu.insert(back_button)
#
# # Halol Burger uchun keyboard
# halolburgMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# halolburgMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# halolburgMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# halolburgMenu.insert(back_button)
#
#
# # Big burger uchun keyboard
# bigburgerMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# bigburgerMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# bigburgerMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# bigburgerMenu.insert(back_button)
#
# # Big Cheeseburger uchun keyboard
# bigcheeseMenu=InlineKeyboardMarkup(row_width=2)
# big=InlineKeyboardButton(text="🛍 Buyurtma berish", callback_data=lavbig_callback.new(item_name="big"))
# bigcheeseMenu.insert(big)
#
# boshm=InlineKeyboardButton(text="📞 Qo'ng'iroq qilish", callback_data="boshmen")
# bigcheeseMenu.insert(boshm)
#
# back_button=InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="cancel")
# bigcheeseMenu.insert(back_button)
