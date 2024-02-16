from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def subsButton(channels, values):
    btnInl = InlineKeyboardMarkup(row_width=1)
    i = 0
    for channel in channels:
        btnKeyboard = InlineKeyboardButton(text=channel, url=values[i])
        btnInl.insert(btnKeyboard)
        i += 1
    azoCheck = InlineKeyboardButton("Obunani tekshirish", callback_data="check_subs")
    btnInl.insert(azoCheck)
    return btnInl


async def yes_no_btn():
    btnInl = InlineKeyboardMarkup(row_width=2)
    btnInl.insert(InlineKeyboardButton("Ha", callback_data="yes"))
    btnInl.insert(InlineKeyboardButton("Yo'q", callback_data="no"))
    return btnInl


def rate_btn():
    btnInl = InlineKeyboardMarkup(row_width=5)
    for i in range(10):
        btnInl.insert(InlineKeyboardButton(f"{i + 1}", callback_data=f"rate_{i + 1}"))
    return btnInl
