from aiogram import types

from loader import dp

from BillyBobBot.utils.billyBobBot import BillyBobBot

key = 0


@dp.message_handler(lambda message: message.text.isdigit())
async def set_offset(message: types.Message):
    global key
    key = int(message.text)
    await message.answer("Сдвиг для шифра установлен.\n\n"
                         "Вы можете поменять его, снова отправив мне число")
    return

@dp.message_handler()
async def encrypt(message: types.Message):
    if key == 0:
        await message.answer("Пожалуйста, установите сдвиг.")
        return
    bob = BillyBobBot(message.text, key)
    await message.answer(bob.encrypt)
    return
