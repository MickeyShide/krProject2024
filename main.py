import asyncio

import dp as dp
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import Message

TOKEN = '6476560422:AAH054CouMc0gItojp0vCYctmXkp-10T1z8'


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    assert isinstance(bot)
    await dp.start_polling(bot)
@dp.message(Command("start"))
async def begin(message: types.Message):
    await message.answer("Пришли фотку лох")
@dp.message(F.animation)
async def echo_gif(message: Message):
    await message.reply_animation(message.animation.file_id)


if __name__ == "__main__":
    asyncio.run(main())