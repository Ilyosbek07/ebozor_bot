from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.TilKeyboards import btn


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"👋 <b>Assalomu alaykum, <i> {message.from_user.full_name}!\n\nO'zingiz uchun qulay bo'lgan tilni tanlang:</i></b>", reply_markup=btn)


