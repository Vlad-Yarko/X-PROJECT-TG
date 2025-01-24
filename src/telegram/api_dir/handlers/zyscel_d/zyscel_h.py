from pyrogram.filters import chat, media_group, photo, video
from pyrogram import Client
from pyrogram.types import Message
from src.telegram.api_dir.handlers.zyscel_d.patterns import make_product



def reg_z(app):
    @app.on_message(chat('zyscel_test') & media_group)
    async def get_post_group(client: Client, message: Message):
        if message.caption is not None:
            text = message.caption
            p = message.photo.file_id
        try:
            if not text:
                return
            if not any(element in text for element in tuple('abcdefghijklmnopqrstuvwxyz')):
                return
            await make_product(text=text, photo=p, message_id=message.id)
        except UnboundLocalError:
            pass

    @app.on_message(chat('zyscel_test') & photo)
    async def get_post_photo(client: Client, message: Message):
        text = message.caption
        p = message.photo.file_id
        if not text:
            return
        if not any(element in text for element in tuple('abcdefghijklmnopqrstuvwxyz')):
            return
        await make_product(text=text, photo=p, message_id=message.id)

    @app.on_message(chat('zyscel_test') & video)
    async def get_post_video(client: Client, message: Message):
        text = message.caption
        p = 'No photo'
        if not text:
            return
        if not any(element in text for element in tuple('abcdefghijklmnopqrstuvwxyz')):
            return
        await make_product(text=text, photo=p, message_id=message.id)

