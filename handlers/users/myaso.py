from aiogram import types
from keyboards.inline.klaviaturaKeyboard import klaviaturaMenu
from loader import dp

@dp.message_handler(text_contains="🧆 Myaso")
async def select_category(message: types.Message):
    await message.answer("<b><i>👏 Ajoyib! Siz MYASO tanladingiz!</i></b>")
    photo_id="AgACAgIAAxkBAAIHO2LgNdETz9cjlW9EIkEeE5hEiZJnAAKNujEbIWAJS5CUE74ISt3AAQADAgADeAADKQQ"
    await message.answer_photo(
        photo_id, caption=f"<b><i>👏 Ajoyib! Siz MYASO tanladingiz!\n🤔 Nechta buyurtma beramiz?</i></b>", reply_markup=klaviaturaMenu)