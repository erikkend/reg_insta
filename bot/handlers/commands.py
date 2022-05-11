from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from sqlalchemy.exc import IntegrityError

from bot.db.model import Account
from bot.keyboards import choose_soc_net

from sqlalchemy import insert, update


async def cmd_start(message: types.Message):
    await message.answer("Хеллоу", reply_markup=choose_soc_net())


def register_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
