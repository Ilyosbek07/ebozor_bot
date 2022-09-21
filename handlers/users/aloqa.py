from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from loader import  dp

@dp.message_handler(Text(equals='📞  Aloqa', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply("<b><i>Bizning telefon raqamimiz:\n\n📞  +998(97) 076 00 01\n📞  +998(93) 609 01 23\n\n👉  Ijtimoiy tarmoqlarimiz:\n\nTelegram: https://t.me/halol_burger_termiz\n\nInstagram: https://instagram.com/halol_burger_termiz</i></b>")


@dp.message_handler(text='✍️ Fikr bildirish')
async def set_state(msg: types.Message, state: FSMContext):
    await state.set_state('fikr')
    await msg.reply("<b><i>Bizning taomlarimiz yoki Bot faoliyati haqida taklif va etirozlaringiz bo'lsa, ushbu bo'limga batafsil yozib yuboring! Biz jamoamiz bilan albatta sizning fikr va mulohazalaringizni o'rganib chiqamiz!\n\n👉  Dasturchi: @Islomjon_0098</i></b>")

@dp.message_handler(state='fikr')
async def set_state(message: types.Message, state: FSMContext):
    await message.reply(f"<b><i>👋 Rahmat! {message.from_user.full_name}!\n Sizning murojaatingizni qabul qildik!\n Tez orada ushbu murojaatingizni ko'rib chiqamiz!</i></b>")
    await state.finish()

