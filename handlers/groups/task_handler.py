from asyncio import sleep
import re
from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.subcribInline import rate_btn
from loader import dp, bot
from utils.db_api.model import new_user_add


@dp.message_handler(lambda message: re.search(r'#task', message.text, re.IGNORECASE))
async def task_func(message: types.Message):
    if message.reply_to_message:
        await message.answer(message.reply_to_message.text)
    else:
        await message.answer(message.text)
