from loader import dp
from aiogram import types
from keyboards.inline.mainKey import back
from keyboards.inline.convertKey import ckey
from utils.calldata import convertCall
from utils.api import getCur



@dp.callback_query_handler(text='convert')
async def convertHandler(call : types.CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.delete()
    await call.message.answer("Konvertatsiya qilish uchun shunchaki summa yuboring va valyutalarni tanlang", reply_markup=back)



@dp.message_handler(lambda msg: float(msg.text.replace(' ','')))
async def converter(msg: types.Message):
    await msg.answer(f"Konvertatsiya yo'nalishini tanlang▼", reply_markup=ckey(msg.text.replace(' ','')))

@dp.callback_query_handler(convertCall.filter())
async def convertSum(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.delete()
    # print(getCur(callback_data.get('fromc'))['conversion_rates'][callback_data.get('to')])
    await call.message.answer(f"{callback_data.get('sum')} {callback_data.get('fromc')} - {getCur(callback_data.get('fromc'))['conversion_rates'][callback_data.get('to')] * float(callback_data.get('sum'))} {callback_data.get('to')}")