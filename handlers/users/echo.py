from aiogram.dispatcher import filters
from aiogram import types
from loader import dp


REGEX = f""

@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def allChat(message: types.Message):
    await message.answer(
        f"<b><i>{message.from_user.full_name}❗\nYouTube Shortsdan video yuklash uchun 🔗 link yuboring!</i></b>")
