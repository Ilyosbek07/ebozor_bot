from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import InputFile
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from keyboards.inline.pittaKeyboard import pittaMenu
from loader import dp


@dp.message_handler(text_contains="Pitta")
async def select_category(message: types.Message):
    await message.answer(f"<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>")
    photo_id="AgACAgIAAxkBAAIG_WLeGALE-FtuFV5CkClAZROzHcD_AALqvjEb3cLxSti2mO6hm6gzAQADAgADeQADKQQ"
    await message.answer_photo(
        photo_id, caption=f"<b><i>PITTA обичний - 22 000 so'm\nBIG  PITTA - 35 000 so'm</i></b>", reply_markup=pittaMenu
    )

    @dp.callback_query_handler(text="pitta")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIG_2LeGBqt-ppDCqwAAc46XO5NfaRE2QAC7L4xG93C8UoLrfn6JYhUSwEAAwIAA3kAAykE"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Pitta obichniy tanladingiz!\n💵 Narxi - 22 000 so'm\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="bigpitta")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIHAWLeGBskSG8199fEOv8ndZRzMOOjAALtvjEb3cLxSm2wvhugULjqAQADAgADeAADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Big Pitta tanladingiz!\n💵 Narxi - 35 000 so'm\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)


    @dp.callback_query_handler(text="cancel")
    async def cancel_buying(call: CallbackQuery):
        await call.message.edit_reply_markup(reply_markup=pittaMenu)
        await call.message.delete()
        await call.answer()