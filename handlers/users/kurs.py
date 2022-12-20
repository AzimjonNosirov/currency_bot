from loader import dp
from aiogram import types
from utils.api import getCur
from keyboards.inline.mainKey import back

currencies = ["USD", "RUB", "EUR", "GBP"]
curData = {
    "USD" : "AQSH dollari",
    "RUB" : "Rossiya rubli",
    "EUR" : "Yevro",
    "GBP" : "Funt sterling",
    
}

@dp.callback_query_handler(text="kurs")
async def sendKurs(call : types.CallbackQuery):
    await call.answer(cache_time=60)
    txt = str()
    for i in currencies:
        txt+=f"""1 {curData[i]} - {getCur(i)["conversion_rates"]["UZS"]} so'm\n"""

    await call.message.answer(txt, reply_markup=back)
    