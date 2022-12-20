from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.calldata import convertCall
def ckey(amount):
    convertKey = InlineKeyboardMarkup(row_width=2)
    convertKey.insert(InlineKeyboardButton(text="🇺🇸USD➡🇺🇿UZS" , callback_data=convertCall.new(fromc="USD", to='UZS', sum=amount)))
    convertKey.insert(InlineKeyboardButton(text="🇺🇿UZS➡🇺🇸USD" , callback_data=convertCall.new(fromc="UZS", to='USD', sum=amount)))
    convertKey.insert(InlineKeyboardButton(text="🇷🇺RUB➡🇺🇿UZS" , callback_data=convertCall.new(fromc="RUB", to='UZS', sum=amount)))
    convertKey.insert(InlineKeyboardButton(text="🇺🇿UZS➡🇷🇺RUB" , callback_data=convertCall.new(fromc="UZS", to='RUB', sum=amount)))
    convertKey.insert(InlineKeyboardButton(text="🇪🇺EUR➡🇺🇿UZS" , callback_data=convertCall.new(fromc="EUR", to='UZS', sum=amount)))
    convertKey.insert(InlineKeyboardButton(text="🇺🇿UZS➡🇪🇺EUR" , callback_data=convertCall.new(fromc="UZS", to='EUR', sum=amount)))
    # 🇺🇿 🇷🇺 🇪🇺 🇺🇸
    return convertKey