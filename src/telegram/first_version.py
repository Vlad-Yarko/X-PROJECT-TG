# @zyscel_router.message(F.media_group_id)
# async def post_album(message: Message):
#     po = list()
#     product = list()
#     if message.caption:
#         po.append(message.caption)
#         if message.photo is not None:
#             po.append(message.photo[-1].file_id)
#         else:
#             po.append(None)
#     if po:
#         product.append(po)
#     try:
#         p = product[0][1]
#         c = product[0][0]
#     except IndexError:
#         pass
#     try:
#         prod = c.split('\n')
#         for i in prod:
#             if i:
#                 print(i)
#         print(p)
#     except UnboundLocalError:
#         pass
#     # try:
#     #     await message.answer_photo(photo=p, caption=c)
#     # except UnboundLocalError:
#     #     pass