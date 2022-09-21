from aiogram.types import CallbackQuery

from keyboards.inline.KofeKeyboard import kofeMenu
from keyboards.inline.choyKeyboard import choyMenu
from keyboards.inline.cocolaMenu import CocacolaMenu
from keyboards.inline.familyKeyboard import familyMenu
from keyboards.inline.fantaKeyboard import fantaMenu
from keyboards.inline.flashKeyboard import flashMenu
from keyboards.inline.ichimliklar import ichimliklarMenu
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from keyboards.inline.nistleKeyboard import nistleMenu
from keyboards.inline.pepsiKeyboard import pepsiMenu
from keyboards.inline.sokKeyboard import sokMenu
from keyboards.inline.spriteKeyboard import spriteMenu
from loader import dp


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ichimliklarMenu)
    await call.message.delete()
    await call.answer()


@dp.callback_query_handler(text="cocacolaa")
async def by_courses(call: CallbackQuery):
    await call.message.answer(
        "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
        reply_markup=CocacolaMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="pepsi0")
async def by_courses(call: CallbackQuery):
    await call.message.answer(
        "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
        reply_markup=pepsiMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

    @dp.callback_query_handler(text="fanta0")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
            reply_markup=fantaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="soklar1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
            reply_markup=sokMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="adrenaline1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz ADRENALINE tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="flash1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
            reply_markup=flashMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="chortoq1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Siz CHORTOQ tanladingiz! \n🤔 Nechta buyurtma beramiz?</i></b>",
            reply_markup=klaviaturaMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="nistle1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
            reply_markup=nistleMenu)
        await call.message.delete()
        await call.answer(cache_time=60)


    @dp.callback_query_handler(text="sprite1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
            reply_markup=spriteMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="familiy1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
            reply_markup=familyMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="choy1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
            reply_markup=choyMenu)
        await call.message.delete()
        await call.answer(cache_time=60)

    @dp.callback_query_handler(text="kofe1")
    async def by_courses(call: CallbackQuery):
        await call.message.answer(
            "<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>",
            reply_markup=kofeMenu)
        await call.message.delete()
        await call.answer(cache_time=60)