from aiogram.types import Message
from  keyboards.default.MenyularKeyboard import menyularKeyboard
from keyboards.default.UzbekKeyboard import menuUzbek
from keyboards.inline.buy_book import book_keys

from loader import  dp

@dp.message_handler(text="🍽 Menyu")
async def send_menyu(message: Message):
    await message.answer("<b>👏  Ajoyib!  Birgalikda buyurtma beramizmi?</b>", reply_markup=menyularKeyboard)

@dp.message_handler(text="📍 Manzil")
async def send_menyu(message: Message):
    await message.answer("<b>👏  Ajoyib!  Keling birgalikda tanlaymiz!</b>", reply_markup=book_keys)

@dp.message_handler(text="🔙 Ortga qaytish")
async def back_link(message: Message):
    await message.answer("<b><i>👏  Ajoyib!  Birgalikda buyurtma beramizmi?</i></b>", reply_markup=menuUzbek)