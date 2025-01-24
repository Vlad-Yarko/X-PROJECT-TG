from aiogram.types import Message
from aiogram import Router, F

from src.telegram.bot_dir.fsm.chanels import Chanel
from src.telegram.bot_dir.handlers.casual_italy_h.ci_patterns import get_all_positions_c


casual_italy_router = Router()
casual_italy_router.message.filter(Chanel.active_casual_italy)


@casual_italy_router.message(F.media_group_id)
async def post_album(message: Message, session):
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
        await get_all_positions_c(c, p, session)
        await message.reply('Success')
        print('----------------------------------')
    except UnboundLocalError:
        pass


@casual_italy_router.message(F.photo)
async def post_photo(message: Message, session):
    c = message.caption
    p = message.photo[-1].file_id
    await get_all_positions_c(c, p, session)
    await message.reply('Success')


@casual_italy_router.message(F.video)
async def post_video(message: Message, session):
    c = message.caption
    p = None
    await message.answer(c, p, session)
