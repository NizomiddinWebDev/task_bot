import asyncio
import time

import aioschedule
from aiogram import executor
from aiogram.types import Message

from keyboards.inline.subcribInline import yes_no_btn
from loader import dp, bot
import middlewares, filters, handlers
from utils.db_api.model import getGroupList
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def noon_print():
    btn = await yes_no_btn()
    groups = await getGroupList()
    for group in groups:
        try:
            await bot.send_message(group.chat_id, "Assalomu alaykum\nBlaze tizimimizdan foydalanayapsizmi?",reply_markup=btn)
        except:
            print("error")


async def scheduler():
    aioschedule.every().minute.do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    asyncio.create_task(scheduler())

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
