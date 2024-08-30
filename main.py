import asyncio
import logging
import sys

import db.models, db.requests
from aiogram import Bot, Dispatcher
from config import TOKEN, LOGS_FILENAME
from handlers import router
from db.models import async_main
bot = Bot(token=TOKEN)
async def main():
    #print("\n\n\n\n\n\n\n\n\n\n")
    #for user in await db.requests.get_users():
    #    user: db.models.Users = user
    #    #print("\n\n\n", user.messages)
    #    for message in user.messages:
    #        message: db.models.Messages = message
    #        print("\n\n\n" + message.text)
    await async_main()
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    #logging.basicConfig(filename=LOGS_FILENAME, filemode="a", level=logging.INFO)
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")