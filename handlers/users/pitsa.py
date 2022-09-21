
from aiogram.types import Message, CallbackQuery

from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from keyboards.inline.pitsaKeyboard import pitsaMenu
from loader import dp

@dp.message_handler(text_contains="Pitsa")
async def select_category(message:Message):
    await message.answer(f"<b><i>Ajoyib! Keling birgalikda tanlaymiz!</i></b>", reply_markup=pitsaMenu)

    @dp.callback_query_handler(text="pitsa1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz MARGARITA pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz GRIBNAYA pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz OVOSHNOY pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa4")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz HALOL PITSA tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa5")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz KURINNAYA GRUDINKA pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa6")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz PEPPERONI pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa7")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz MEKSIKANO pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa8")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz DRAKON pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa9")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz VETCHINA S GRIBAMI pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa10")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz BERBEKYU pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa11")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz FIRMENNAYA pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa12")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz MYASNAYA pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa13")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz 4-MYASO pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa14")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz AMERICANO pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa15")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz SUPER ASSORTI pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa16")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz MIKS pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa17")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz DON KARLEONE pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pitsa18")
    async def by_courses(call: CallbackQuery):
        await call.message.answer("<b><i>👏 Ajoyib! Siz MAFIA pitsasini tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)