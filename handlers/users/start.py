from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.mainKey import mainKey
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! Valyuta konvertori botimizga xush kelibsiz. Marhamat quyidagi bo'limlardan birini tanlang.", reply_markup=mainKey)


@dp.callback_query_handler(text="back")
async def bot_start(call: types.CallbackQuery):
    await call.message.answer(f"Assalomu alaykum, {call.from_user.full_name}! Valyuta konvertori botimizga xush kelibsiz. Marhamat quyidagi bo'limlardan birini tanlang.", reply_markup=mainKey)
