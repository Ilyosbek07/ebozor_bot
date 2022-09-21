
from aiogram.types import Message, CallbackQuery

from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from keyboards.inline.shirinlikKeyboard import shirinlikMenu
from loader import dp

@dp.message_handler(text_contains="Shirinliklar")
async def select_category(message:Message):
    await message.answer(f"<b><i>Ajoyib! Keling birgalikda tanlaymiz!</i></b>", reply_markup=shirinlikMenu)

    @dp.callback_query_handler(text="banana")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>Ajoyib! Siz BANANA shirinligini tanladingiz!</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="maxroviy")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>Ajoyib! Siz MAXROVIY shirinligini tanladingiz!</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="shokoladniy")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>Ajoyib! Siz SHOKOLADNIY shirinligini tanladingiz!</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="piramida")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>Ajoyib! Siz PIRAMIDA shirinligini tanladingiz!</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="lakomka")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>Ajoyib! LAKOMKA shirinligini tanladingiz!</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)


    @dp.callback_query_handler(text="cancel")
    async def cancel_buying(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=shirinlikMenu)
        await call.message.delete()
        await call.answer()