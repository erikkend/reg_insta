import asyncio
import logging

from aiogram import Bot, Dispatcher
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram.types.bot_command_scope import BotCommandScopeDefault
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from db.base import Base
from handlers.commands import register_commands


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начать работу бота"),
        BotCommand(command="stop", description="Пристановить рассылку"),
        BotCommand(command="go", description="Возобновить рассылку"),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    user = "root"
    password = "password"
    host = "127.0.0.1"
    port = "3306"
    dbname = "instagram_accs"
    conn_str = f'mysql+aiomysql://{user}:{password}@{host}:{port}/{dbname}'

    engine = create_async_engine(conn_str)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    async_sessionmaker = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    # expire_on_commit=False will prevent attributes from being expired
    # after commit.

    bot = Bot("5184212708:AAEd-EilYPSAcGvjU2M1-sUcGRcTzcI9Xb0", parse_mode="HTML")
    bot["db"] = async_sessionmaker
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_commands(dp)

    await set_bot_commands(bot)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    logging.error("Bot stopped!")
