from aiogram import Bot, Dispatcher

from dotenv import load_dotenv, find_dotenv

from asyncio import run

import os

from src.telegram.handlers.main_h.base_h import base_command_router, quit_store_router
from src.telegram.cmds import commands
from src.telegram.handlers.zyscel_d.zyscel_h import zyscel_router
from src.telegram.handlers.keshkatura.keshkatura_h import keshkature_router
from src.telegram.middlewares.base_m import ConnDB
from src.telegram.handlers.casual_italy_h.ci_h import casual_italy_router

# from middlewares.base_m import Access

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.message.outer_middleware(ConnDB())
dp.callback_query.outer_middleware(ConnDB())


dp.include_routers(
    base_command_router,
    quit_store_router,
    zyscel_router,
    keshkature_router,
    casual_italy_router
)


async def main():
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)


run(main())
