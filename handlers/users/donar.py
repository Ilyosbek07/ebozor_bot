from aiogram import types
from loader import dp
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu


@dp.message_handler(text_contains="Donar")
async def select_category(message: types.Message):
    await message.answer(f"<b><i>š Ajoyib! Keling birgalikda tanlaymiz!</i></b>")
    photo_id="AgACAgIAAxkBAAIGSGLbipogCHvgAAH3dFP4XgM7hDu0aQACVLwxG8ex4Ep1ZiKfN-hbBwEAAwIAA3gAAykE"
    await message.answer_photo(
        photo_id, caption=f"<b><i>š Ajoyib! Siz DONAR tanladingiz!\nšµ Narxi - 20 000 so'm\nš¤ Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)

