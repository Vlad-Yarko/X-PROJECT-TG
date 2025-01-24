from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from typing import Callable, Dict, Awaitable, Any

from src.telegram.bot_dir.databases.engine import main_session

# from src.telegram.databases.requests import orm_is_admin


# class Access(BaseMiddleware):
#     def __init__(self):
#         pass
#
#     async def __call__(
#             self,
#             handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#             event: TelegramObject,
#             data: Dict[str, Any]):
#         async with main_session() as session:
#             user = await orm_is_admin(session, event.from_user.id)
#             if user:
#                 data['session'] = session
#                 return await handler(event, data)


class ConnDB(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]):
        async with main_session() as session:
            data['session'] = session
            return await handler(event, data)
