from aiogram.types import Message, CallbackQuery

from keyboards.default import joylashuvMenu
from keyboards.default.UzbekKeyboard import menuUzbek
from keyboards.default.location_button import keyboard
from loader import dp


@dp.callback_query_handler(text="mycontact")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="<b><i>👉  Raqamingizni yuborish uchun</i></b> \n<b>📲  Raqamimni yuborish</b> <b><i>tugmasini bosing!</i></b>", reply_markup=keyboard)

@dp.message_handler(content_types='contact')
async def get_contact(message: Message):
    contact = message.contact
    await message.answer(f"<b><i>Rahmat!   {contact.full_name}!.\n</i></b>"
                         f"<b><i>Sizning  </i></b>{contact.phone_number}<b><i>  raqamingizni qabul qilganimizdan mamnunmiz!\n\n 👉  Keyingi bosqichga o'tish uchun joylashuv manzilingizni yuboring! \n‼️  Manzilingizni yuborish uchun telefoningizdagi joylashuv axboroti yoqilgan bo'lishi kerak!</i></b>",
                         reply_markup=keyboard)