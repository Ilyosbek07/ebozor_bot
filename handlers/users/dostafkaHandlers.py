from aiogram.types import Message
from keyboards.default.ruyxatgaOlish import ruyxat
from keyboards.default.savatKeyboard import savatMenu
from loader import  dp

@dp.message_handler(text="🚗  Yetkazib  berish")
async def send_menyu(message: Message):
    await message.answer("<b>Ajoyib!  Birgalikda tanlaymizmi?</b>", reply_markup=ruyxat)


@dp.message_handler(text="↩️ Ortga  qaytish")
async def back_link(message: Message):
    await message.answer("<b><i>Ajoyib!  Birgalikda buyurtma beramizmi?</i></b>", reply_markup=savatMenu)