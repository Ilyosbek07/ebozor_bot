from loader import dp
from aiogram.types import ContentType, Message
from  keyboards.default.MenyularKeyboard import menyularKeyboard
from pathlib import Path

download_path=Path().joinpath("downloads", "catigories")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination=download_path)
    doc_id = message.document.file_id
    await message.reply("Siz hujjat yubordingiz!"
                        f"file_id={doc_id}")


@dp.message_handler(content_types=ContentType.VIDEO)
async def video_handler(message: Message):
    await message.video.download(destination=download_path)
    await message.reply("Siz video yubordingiz!\n"
                        f"file_id={message.video.file_id}")


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: Message):
    await message.photo[-1].download(destination=download_path)
    await message.reply("Siz rasm yubordingiz!\n"
                        f"file_id={message.photo[-1].file_id}")
