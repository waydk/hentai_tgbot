from source.app import bot, dp

import asyncio
from . import handlers

from aiogram import Dispatcher



async def setup_handlers(dp: Dispatcher):
    dp.include_router(handlers.prepare_router())

async def aiogram_on_startup_polling(dispatcher: Dispatcher) -> None:
    await setup_handlers(dispatcher)


async def main() -> None:
   
    dp.startup.register(aiogram_on_startup_polling)
    await dp.start_polling(bot)

    
if __name__ == '__main__':
    
    asyncio.run(main())