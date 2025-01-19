from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.telegram.databases.models import MyProduct

# from src.telegram.databases.models import User, TGProduct, Yep


# async def orm_is_admin(session, tg_id):
#     data = await session.execute(select(User).where(User.tg_id == tg_id))
#     user = data.scalar()
#     if not user is None:
#         if user._is_admin:
#             return True
#         else:
#             return False
#     else:
#         return False


# async def orm_add_trash(caption, photo):
#     async with main_session() as session:
#         await session.execute(insert(Yep).values(caption=caption, photo=photo))
#         await session.commit()
#         # await session.execute(delete(Yep).where(Yep.caption == ""))
#         # await session.commit()


async def orm_add_product(session: AsyncSession, photo, source, title, size, description, price, state, available):
    await session.execute(insert(MyProduct).values(source=source,
                                                   title=title,
                                                   size=size,
                                                   description=description,
                                                   price=price,
                                                   state=state,
                                                   available=available,
                                                   image=photo))
    # await session.execute(insert(MyImage).values(data=photo, product_id=3))
    await session.commit()
