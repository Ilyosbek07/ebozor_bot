from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default.UzbekKeyboard import menuUzbek
from keyboards.default.location_button import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp


@dp.callback_query_handler(text="mylocation")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="<b>🏠  Eng yaqin manzilimizni bilmoqchi bo'lsangiz,  joylashuv manzilingizni botga yuboring!\n\n👉 <i>Manzilingizni yuborish uchun telefoningizdagi joylashuv axboroti yoqilgan bo'lishi kerak!</i></b>", reply_markup=keyboard)
    await call.answer(cache_time=60)


@dp.message_handler(content_types='location')
async def get_contact(message: Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location)

    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n Masofa: {distance:.1f} km."
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"<b><i>Rahmat!   {message.from_user.full_name}!\n\nSizga eng yaqin masofamiz!         </i></b>\n👇👇👇👇👇👇👇👇👇\n\n"
                         f"Latitude = {latitude}\n"
                         f"Longitude = {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=menuUzbek)

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])

@dp.message_handler(text="🔙 Ortga qaytish")
async def back_link(message: Message):
    await message.answer("<b><i>Ajoyib!  Birgalikda buyurtma beramizmi?</i></b>", reply_markup=menuUzbek)
    await call.answer(cache_time=60)
