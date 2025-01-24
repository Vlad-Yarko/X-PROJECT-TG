from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import StateFilter

from src.telegram.bot_dir.fsm.chanels import Chanel
from src.telegram.bot_dir.handlers.zyscel_d.patterns import get_all_positions_z


zyscel_router = Router()
zyscel_router.message.filter(StateFilter(Chanel.active_zyscel))


@zyscel_router.message(F.media_group_id)
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
        if p is None:
            p = 'No image'
    except IndexError:
        pass

    try:
        await get_all_positions_z(c, p, session)
        await message.reply('Success')
        print('----------------------------------')
    except UnboundLocalError:
        pass


@zyscel_router.message(F.photo)
async def post_photo(message: Message, session):
    c = message.caption
    p = message.photo[-1].file_id
    await get_all_positions_z(c, p, session)
    await message.reply('Success')


@zyscel_router.message(F.video)
async def post_video(message: Message, session):
    c = message.caption
    p = "No image"
    await get_all_positions_z(c, p, session)
    await message.reply('Success')
