from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

mainKey = InlineKeyboardMarkup(row_width=1)
mainKey.insert(InlineKeyboardButton("💹Valyutalar kursi", callback_data='kurs'))
mainKey.insert(InlineKeyboardButton("💱Konvertor", callback_data='convert'))

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Orqaga", callback_data="back")
        ],
    ],
)