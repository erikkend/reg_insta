from aiogram import types
from common import cb_data


def choose_soc_net():
    kb = types.InlineKeyboardMarkup(row_width=2)

    kb.add(types.InlineKeyboardButton(text="Вконтакте", callback_data="vk"),
           types.InlineKeyboardButton(text="Instagram", callback_data="inst"))

    return kb
