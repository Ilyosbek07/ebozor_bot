from aiogram import types
from aiogram.types import Message
from keyboards.default.SozlamaKeyvoard import language
from keyboards.inline.TilKeyboards import btn

from loader import  dp

@dp.message_handler(text="⚙️ Sozlamalar")
async def send_menyu(message: Message):
    await message.answer("<b>👉  Tilni almashtirish uchun <i>🌐  Tilni  almashtirish</i>  tugmasini bosing</b>", reply_markup=language)

@dp.message_handler(text="🌐  Tilni  almashtirish")
async def bot_lang(message: types.Message):
    await message.answer(f"👋 <b>Assalomu alaykum, <i> {message.from_user.full_name}!\n\nO'zingiz uchun qulay bo'lgan tilni tanlang:</i></b>", reply_markup=btn)

@dp.message_handler(text="🔙 Ortga qaytish")
async def back_link(message: Message):
    await message.answer("<b><i>Ajoyib!  Birgalikda buyurtma beramizmi?</i></b>", reply_markup=menuUzbek)
    await call.answer(cache_time=60)
