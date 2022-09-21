from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import InputFile
from keyboards.inline.hotDogKeyboard import hotdogMenu
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from loader import dp


@dp.message_handler(text_contains="🌭 Hot-Dog")
async def select_category(message: types.Message):
    await message.answer(f"<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>")
    photo_id="AgACAgIAAxkBAAIGYmLbrpgvmFf5sBU_bOec7CsEWVztAAKevDEbx7HgSsi5xMt_8uR0AQADAgADeAADKQQ"
    await message.answer_photo(
        photo_id, caption=f"<b><i>Hot Dog obichniy - 8 000 so'm\nChiz  Dog - 10 000 so'm\nKorolevskiy - 12 000 so'm\nHot Dog Myasnoy - 18 000 so'm</i></b>", reply_markup=hotdogMenu)


    @dp.callback_query_handler(text="hotdog")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIGeGLbsJRNaCX0DAt7D47-XRVLVLNSAAKkvDEbx7HgSsPQlxOecDcVAQADAgADeAADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b>👏 Ajoyib! Siz Hot Dog obichniy tanladingiz!\n💵 Narxi - <i>8 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="chisdog")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIGcmLbsFJAq0rYtUljNhWPckWI7XWuAAKhvDEbx7HgSrlxEaSs5jyDAQADAgADeQADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Chis-Dog tanladingiz!\nNarxi - <i>10 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="korolevskiy")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIGdGLbsGZyWLt9Fi6BYZo5S_qyvbBtAAKivDEbx7HgSo9UyeD94fF9AQADAgADeQADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Hot-Dog Korolevskiy tanladingiz!\n💵 Narxi - <i>12 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="hotdogmyasnoy")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIGdmLbsHeGaYRdj4vY1IO5wM-Fyg9OAAKjvDEbx7HgSnY-GMzPFp3QAQADAgADeQADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Go'shtli Hot-Dog tanladingiz!\n💵 Narxi - <i>18 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)


    # @dp.callback_query_handler(text="boshmen")
    # async def by_courses(call: CallbackQuery):
    #     await call.message.answer("<b><i>Bizning telefon raqamimiz:</i></b>\n\n📞  +998970760001\n\n📞  +998936090123")
    #     await call.answer(cache_time=60)

    @dp.callback_query_handler(text="cancel")
    async def cancel_buying(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=hotdogMenu)
        await call.answer()