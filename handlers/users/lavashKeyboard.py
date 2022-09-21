from aiogram import types
from keyboards.inline.productsKeyboard import categoryMenu
from loader import dp, bot

@dp.message_handler(text="🌯️ Lavash")
async def send_book(message: types.Message):
    await message.answer(f"<b><i>👏 Ajoyib! Keling birgalikda tanlaymiz!</i></b>")
    photo_id = "AgACAgIAAxkBAAPXYtefS6Hsy__xqLISUqYLP8GjTmwAAly7MRsIfcBKbch20hUE5l8BAAMCAAN5AAMpBA"
    await message.answer_photo(
        photo_id, reply_markup=categoryMenu,
    )
    await bot.send_photo(
        chat_id=message.from_user.id,
    )
