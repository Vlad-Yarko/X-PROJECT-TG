from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import StateFilter

from src.telegram.fsm.chanels import Chanel
from src.telegram.handlers.keshkatura.patterns_k import get_all_positions_k


keshkature_router = Router()
keshkature_router.message.filter(StateFilter(Chanel.active_keshtatura))


@keshkature_router.message(F.media_group)
async def post_album_k(message: Message, session):
    po = list()
    product = list()
    if message.caption:
        po.append(message.caption)
        if message.photo is not None:
            po.append(message.photo[-1].file_id)
        else:
            po.append(None)
    if po:
        product.append(po)
    try:
        p = product[0][1]
        c = product[0][0]
    except IndexError:
        pass
    try:
        await get_all_positions_k(c, p, session)
        await message.reply('Success')
        print('----------------------------------')
    except UnboundLocalError:
        pass


@keshkature_router.message(F.photo)
async def post_photo(message: Message, session):
    c = message.caption
    p = message.photo[-1].file_id
    await get_all_positions_k(c, p, session)
    await message.reply('Success')


@keshkature_router.message(F.video)
async def post_video(message: Message, session):
    c = message.caption
    p = None
    await get_all_positions_k(c, p, session)
    await message.reply('Success')
