import time

from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from utils.db_api.model import new_user_add


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def save_group_id(message: types.Message):
    if bot.id in [member.id for member in message.new_chat_members]:
        group_id = message.chat.id
        try:
            await new_user_add(group_id, 'group')
        except:
            pass
        text = f"<b><i>Assalomu alaykum,Men Support Botman</b>"
        await message.answer(text)


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.SUPERGROUP))
async def show_channels(message: types.Message):
    try:
        await new_user_add(message.chat.id, 'group')
    except:
        pass
    text = f"<b><i>Assalomu alaykum, {message.from_user.full_name}\n\nInstagramdan video yuklash uchun 🔗 link yuboring!!!</i></b>"
    await message.answer(text)


@dp.message_handler(CommandStart(), filters.ChatTypeFilter(types.ChatType.GROUP))
async def show_channels(message: types.Message):
    try:
        await new_user_add(message.chat.id, 'group')
    except:
        pass
    text = f"<b><i>Assalomu alaykum, {message.from_user.full_name}\n\nInstagramdan video yuklash uchun 🔗 link yuboring!!!</i></b>"
    await message.answer(text)
