
from aiogram.types import Message, CallbackQuery

from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from keyboards.inline.nonDog import nonDogMenu
from loader import dp

@dp.message_handler(text_contains="Non-Dog")
async def select_category(message:Message):
    await message.answer(f"<b><i>š Ajoyib! Keling birgalikda tanlaymiz!</i></b>", reply_markup=nonDogMenu)


    @dp.callback_query_handler(text="nondog")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz Non-Dog tanladingiz!\nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)


    @dp.callback_query_handler(text="nonburger")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>š Ajoyib! Siz Non Burger tanladingiz!\nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)


    @dp.callback_query_handler(text="cancel")
    async def cancel_buying(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=nonDogMenu)
        await call.message.delete()
        await call.answer()