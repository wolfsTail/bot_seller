import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from middleware.db import DataBaseMiddleware
from handlers.user_privat import user_private_router
from handlers.user_group import user_group_router
from handlers.admin_panel import admin_router
from database.engine import create_db, drop_db, session_maker



bot = Bot(token=os.getenv('TOKEN'), parse_mode="HTML")
bot.my_admins_list = []

dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)


async def on_startup(bot):    

    # await drop_db()  # for start up if have any data in db
    
    await create_db()

async def on_shutdown(bot):
    print("Bot is shuting down")


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseMiddleware(session_pool=session_maker))
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    # await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


asyncio.run(main())