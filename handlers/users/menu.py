from aiogram.types import Message, CallbackQuery
from  keyboards.default.UzbekKeyboard import menuUzbek
from keyboards.default.contact_button import keyboard

from loader import  dp

@dp.callback_query_handler(text="uz")
async def send_link(call: CallbackQuery):
    await call.message.answer(f"<b>👏  Ajoyib!  Qaysi bo'limni tanlaymiz?</b>", reply_markup=menuUzbek)

@dp.message_handler(text="🔙 Ortga qaytish")
async def back_link(message: Message):
    await message.answer("<b><i>Ajoyib!  Qaysi bo'limni tanlaymiz?</i></b>", reply_markup=menuUzbek)
    await call.answer(cache_time=60)
