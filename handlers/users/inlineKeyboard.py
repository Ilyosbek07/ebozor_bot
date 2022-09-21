from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import InputFile
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from keyboards.inline.productsKeyboard import categoryMenu
from loader import dp

@dp.message_handler(text="🌯️ Lavash")
async def send_lavash(message: types.Message):
    await message.answer(f"<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>")
    photo_id = "AgACAgIAAxkBAAIBZ2MmyujRMLPzJUXUk-mhKu5FvGzAAAKSwjEbmeI4SQAB-FriO9RbuwEAAwIAA3kAAykE"
    await message.answer_photo(
        photo_id, caption="<b>Lavash obichniy - <i>22 000 so'm</i>\nLavash Pishloqli - <i>24 000 so'm</i>\nBIG Lavash - <i>35 000 so'm</i>\nTandir Lavash - <i>24 000 so'm</i>\nBIG Tandir Lavash - <i>40 000 so'm</i></b>", reply_markup=categoryMenu)

    @dp.callback_query_handler(text="lavashshsh")
    async def by_courses(call: CallbackQuery):
        photo_id = "AgACAgIAAxkBAAIBbmMmy5Sg29SlhpliCigq8xJXlA0BAAKWwjEbmeI4STOapwABLXPVtQEAAwIAA3kAAykE"
        await message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Lavash obichniy tanladingiz!\n💵 Narxi - <i>22 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="lavashpishloq")
    async def by_courses(call: CallbackQuery):
        photo_id = "AgACAgIAAxkBAAIDqWLZNl2pqZJkDcy19XxnLwyRrf0CAALPvTEbNtrJSqLriCnpycX_AQADAgADeQADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Pishloqli Lavash tanladingiz!\n💵 Narxi - <i>24 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="lavashbig")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIEDWLZi9eQ0dm8_E0vya2PHhphJYd1AAKkvDEbNtrRShRM0XdKnRqWAQADAgADeQADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz BIG Lavash tanladingiz!\n💵 Narxi - <i>35 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="lavashtandir")
    async def by_courses(call: CallbackQuery):
        photo_id="AgACAgIAAxkBAAIER2LZmxaEsmatUjnnlMDzgaigtCzzAALwvDEbNtrRSr1x6uz5ykFBAQADAgADbQADKQQ"
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz Tandir Lavash tanladingiz!\n💵 Narxi - <i>24 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="lavashbigtandir")
    async def by_courses(call: CallbackQuery):
        photo_id = "AgACAgIAAxkBAAIFYmLaRAKmrpp4AblraB41hRj-XHF1AAK6vDEbcrLQSjpNt4GUaBMCAQADAgADeAADKQQ" \
                   "" \
                   ""
        await call.message.answer_photo(
            photo_id, caption="<b><i>👏 Ajoyib! Siz BIG Tandir Lavash tanladingiz!\n💵 Narxi - <i>40 000 so'm</i>\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="cancel")
    async def cancel_buying(call: CallbackQuery):
        await message.answer(f"<b><i>Ajoyib! Keling birgalikda tanlaymiz!</i></b>", reply_markup=categoryMenu)
        await call.message.delete()
        await call.answer(cache_time=60)