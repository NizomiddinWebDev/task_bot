import re
from aiogram import types
from loader import dp, bot
from utils.api.task import create_task


@dp.message_handler(lambda message: re.search(r'#task', message.text, re.IGNORECASE))
async def task_func(message: types.Message):
    if message.reply_to_message:
        status = create_task(chat_id=message.chat.id, description=message.reply_to_message.text)
    else:
        create_task(chat_id=message.chat.id, description=message.text)
