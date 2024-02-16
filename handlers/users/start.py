from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startKeyboard import start_button
from loader import dp, bot
from utils.db_api.model import new_user_add


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.PRIVATE))
async def show_channels(message: types.Message):
    try:
        await new_user_add(message.from_user.id, 'user')
        text = f"<b>Assalomu alaykum! Pronova.uz maktabiga xush kelibsiz.\n\nЗдравствуйте! Добро пожаловать в школу " \
               f"Pronova.uz!</b>"
        await message.answer(text, reply_markup=start_button)
    except:
        pass

