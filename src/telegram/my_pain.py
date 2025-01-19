# from aiogram import Router, F, Bot
# from aiogram.types import Message
# from aiogram.filters import Command
# from aiogram_album.methods.forward_messages import ForwardMessages
# from aiogram_album import AlbumMessage
# from src.telegram.databases.requests import orm_add_trash
# from aiogram.exceptions import TelegramBadRequest
#
#
# # @base_command_router.message(F.media_group_id)
# async def ko(message: Message, bot: Bot):
#     # a = ""
#     # b = ""
#     # if message.caption is not None:
#     #     a += message.caption
#     #     b += message.photo[-1].file_id
#     # print(a)
#     # print('-----')
#     # await orm_add_trash(a, str(b))
#     # a = 0
#     # for i in message:
#     #     print(a, i)
#     #     a += 1
#     # photos = message.photo
#     #
#     # if photos:
#     #     # Отримати перше фото
#     #     first_photo = photos[-1]  # Найвища якість (останній елемент)
#     #     file_id = first_photo.file_id
#     #
#     #     await message.reply(f"File ID першої фотки: {file_id}")
#
#     global caption, photo
#     po = list()
#     product = list()
#     # if message.photo:
#     #     po.append(message.photo[-1].file_id)
#     if message.caption:
#         po.append(message.caption)
#         po.append(message.photo[-1].file_id)
#     # print(po)
#
#     # print('-----')
#     #
#     # if po:
#     #     product.append(po)
#     # print(product)
#     if po:
#         product.append(po)
#
#     try:
#         p = product[0][1]
#         c = product[0][0]
#     except IndexError:
#         pass
#     try:
#         print(c)
#         print(p)
#     except UnboundLocalError:
#         pass
#     # print(caption)
#     # print(photo)
#
#     # try:
#     #     await message.answer_photo(photo=p, caption=c)
#     # except TelegramBadRequest:
#     #     pass
#
#     try:
#         await message.answer_photo(photo=p, caption=c)
#     except UnboundLocalError:
#         pass
#
#     print()
#     # try:
#     #     prod = c.split('\n')
#     #     for i in prod:
#     #         if i:
#     #             print(i)
#     #     print(p)
#     # except UnboundLocalError:
#     #     pass
#     # try:
#     #     await message.answer_photo(photo=p, caption=c)
#     # except UnboundLocalError:
#     #     pass
#     # try:
#     #     if p:
#     #         print(c)
#     #         await session.execute(insert(Yep).values(caption=c, photo=p))
#     #     else:
#     #         print(c)
#     #         await session.execute(insert(Yep).values(caption=c))
#     # except UnboundLocalError:
#     #     pass
#     # await session.commit()