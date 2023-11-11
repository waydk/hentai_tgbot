from loguru import logger
from aiogram.types import Message

"""
Stores all commands that can be executed by the bot
"""

async def start(message: Message):
    user_id = message.from_user.id
    logger.info(f'User send /start {user_id}')
    user_name = message.from_user.first_name
    await message.answer(f'Приветствую, {user_name}')
