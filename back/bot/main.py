from aiogram import Bot, Dispatcher, types
from aiogram.methods import DeleteWebhook
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove

import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TG_TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command(commands="start"))
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="/start",
                           reply_markup=ReplyKeyboardRemove())


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
