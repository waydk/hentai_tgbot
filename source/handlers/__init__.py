from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.filters import Command


from . import commands


def prepare_router() -> Router:
    """
    function for registering commands
    """
    user_router = Router()

    user_router.message.register(commands.start, CommandStart())

    return user_router