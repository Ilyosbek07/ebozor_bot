from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import InputFile
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from keyboards.inline.burgerKeyboard import burgerMenu
from loader import dp


@dp.message_handler(text_contains="🍔  Burger")
async def select_category(message: types.Message):
    await message.answer(f"<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>")
    photo_id="AgACAgIAAxkBAAIBS2MmyZNxYUFqvEg-2aDjxWOP_PXsAAKJwjEbmeI4SUHtsRthrJ2UAQADAgADeQADKQQ"
    await message.answer_photo(
        photo_id, caption=f"<b><i>Gamburger - <i>19 000 so'm</i>\nCheeseburger - <i>24 000 so'm</i>\nHALOL  BURGER - <i>22 000 so'm</i>\nBIG Burger - <i>24 000 so'm</i>\nBIG Cheeseburger - <i>26 000 so'm</i></i></b>", reply_markup=burgerMenu)

    @dp.callback_query_handler(text="gamburg")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIFsmLa_xDFcKd877cAARJgQGDlaVgbtwACpbwxG3Ky2EqWc5a-VIP64QEAAwIAA3kAAykE"
        await call.message.answer_photo(
            photo_id, caption="<b>👏  Ajoyib! Siz Gamburger tanladingiz!\n💵 Narxi - <i>19 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="cheeseburg")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIFwGLa__-IVPPH6LvcojfMprdG5S_MAAKmvDEbcrLYSlfobdHmDBt1AQADAgADeAADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Cheeseburger tanladingiz!\n💵 Narxi - <i>24 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="burgerhalol")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIFzGLbAAGJrK6PkKA-XT3xxd8FRxeUdwACp7wxG3Ky2ErLnjPi_mLZ9QEAAwIAA3kAAykE"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Halol Burger tanladingiz!\n💵 Narxi - <i>22 000 so'm</i>\n🤔 Nechta buyurtma beramiz? </i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="bigburger")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIFzmLbAAGTPNzNB_i1b9d9XL2EhHv82wACqLwxG3Ky2EqZibw12zGbuQEAAwIAA3gAAykE"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz BIG Burger tanladingiz!\n💵 Narxi - <i>24 000 so'm</i>\n🤔 Nechta buyurtma beramiz? </i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="bigcheeseburger")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIBP2MmyQ5Dx2H3NPbw9V3jtDFH3fv5AAICvDEbwTogSarUUUQWeWcMAQADAgADeQADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz BIG Cheeseburger tanladingiz!\n💵 Narxi - <i>26 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="cancel")
    async def cancel_buying(call: CallbackQuery):
        await message.answer(reply_markup=burgerMenu)
        await call.message.delete()
        await call.answer()