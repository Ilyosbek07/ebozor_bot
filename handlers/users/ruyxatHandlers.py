from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.UzbekKeyboard import menuUzbek
from keyboards.default.dostafkaKeyboard import dostafkaMenu
from keyboards.default.savatKeyboard import tulovMenu
from loader import dp, bot
from states.personalData import PersonalData
from aiogram.dispatcher.filters import Regexp

PHONE_NUM=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text="🛍 Buyurtmani tasdiqlash", state=None)
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting:")
    await PersonalData.fullName.set()


@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Telefon raqamingizni kiriting:")

    # await PersonalData.email.set()
    await PersonalData.next()

@dp.message_handler(Regexp(PHONE_NUM), state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )

    await message.answer("Byurtma turini tanlang:", reply_markup=tulovMenu)

    await PersonalData.next()


@dp.message_handler(state=PersonalData.byurtma)
async def answer_byurtma(message: types.Message, state: FSMContext):
    byurtma = message.text

    await state.update_data(
        {"byurtma": byurtma}
    )

    await message.answer("To'lov turini tanlang:", reply_markup=dostafkaMenu)

    await PersonalData.next()


@dp.message_handler(state=PersonalData.tulov)
async def answer_tulov(message: types.Message, state: FSMContext):
    tulov = message.text

    await state.update_data(
        {"tulov" : tulov}
    )

    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    byurtma = data.get("byurtma")
    tulov = data.get("tulov")

    msg = "<b>🧾 Quyidagi ma`lumotlar qabul qilindi:\n\n</b>"
    msg += f"<b><i>👤 Ism:  - </i>  {name}\n\n"
    msg += f"<i>📱 Telefon raqam:  -  </i> {phone}\n\n"
    msg += f"<i>🛍 Byurtma turi:  - </i>  {byurtma}\n\n"
    msg += f"<i>💸 To'lov turi:  -  </i> {tulov}\n\n<i> 📡 Kanalimizga a'zo bo'ling: 👇\n\n✅ Kanal:</i>  @halol_burger_termiz</b>"
    await message.answer(msg)
    await message.answer("<b><i>📨 Sizning byurtmangiz qabul qilindi. Qisqa fursatlarda siz bilan bog'lanamiz!  \nE'tiboringiz uchun Rahmat!</i></b>", reply_markup=menuUzbek)
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    # State dan chiqaramiz
    # 1-variant
    await state.finish()

    # 2-variant
    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)


