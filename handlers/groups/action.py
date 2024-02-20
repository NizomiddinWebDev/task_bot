from asyncio import sleep

from aiogram import types
from keyboards.inline.subcribInline import rate_btn
from loader import dp, bot


@dp.callback_query_handler(text='yes')
async def yes(call: types.CallbackQuery):
    await call.message.delete()
    btn = rate_btn()
    await call.message.answer("Sistemamizni 1 dan 10 gacha baholang!", reply_markup=btn)


@dp.callback_query_handler(text='no')
async def yes(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Foydalanmayotganingiz sababini yozing")


@dp.callback_query_handler(text_startswith='rate_')
async def yes(call: types.CallbackQuery):
    await call.message.delete()
    rate = call.data.split("_")[1]
    await call.message.answer(f"Bahoingiz uchun Rahmat!")
    await sleep(1)
    await call.message.answer(f"Qo'shimcha savol yoki muammongiz  bo'lsa yozib qoldiring!")
