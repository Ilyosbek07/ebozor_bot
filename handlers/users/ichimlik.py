
from aiogram.types import Message, CallbackQuery

from keyboards.inline.ichimliklar import ichimliklarMenu
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu

from loader import dp

@dp.message_handler(text_contains="Ichimliklar")
async def select_category(message:Message):
    await message.answer(f"<b><i>👏  Ajoyib! Keling birgalikda tanlaymiz!</i></b>", reply_markup=ichimliklarMenu)



    @dp.callback_query_handler(text="coca")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
         "<b><i>👏 Ajoyib! Siz COCACOLA 0,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="cocal")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz COCACOLA 1 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="cocala")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz COCACOLA 1,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pepsi5")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
         "<b><i>👏 Ajoyib! Siz PEPSI 0,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pepsi2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
          "<b><i>👏 Ajoyib! Siz PEPSI 1 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="pepsi3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
                "<b><i>👏 Ajoyib! Siz PEPSI 1,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
                reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="fanta5")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz FANTA 0,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="fanta2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz FANTA 1 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="fanta3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz FANTA 1,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="bliss1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz BLISS tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="dena1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz DENA tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="rich1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz RICH tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="flashbig")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz FLASH BIG tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="flashmini")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz FLASH MINI tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)


    @dp.callback_query_handler(text="nistle2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz NISTLE 0,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="nistle3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz NISTLE 1 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="nistle4")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz NISTLE 1,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="sprite2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz SPRITE 0,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="sprite3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz SPRITE 1 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="sprite4")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz SPRITE 1,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="sprite5")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz SPRITE CAN tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="family2")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz FAMILY 0,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="family3")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz FAMILY 1 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="family4")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz FAMILY 1,5 lt tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="kokchoy")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz KO'K  CHOY tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="qorachoy")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz QORA  CHOY tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="limonchoy")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz LIMON  CHOY tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="maccoffe")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz MACCOFFE  tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="nescafegold")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz NESCAFE  GOLD tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="nescafeclassic")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz NESCAFE  CLASSIC tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="jacobs")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz JACOBS tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)