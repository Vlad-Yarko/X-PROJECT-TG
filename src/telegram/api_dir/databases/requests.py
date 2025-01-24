from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.telegram.api_dir.databases.engine import main_session

from src.telegram.api_dir.databases.models import MyProduct

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


async def orm_add_product(photo: str,
                          brand: str,
                          price_range: str,
                          currency: str,
                          channel_name: str,
                          title: str,
                          size: str,
                          description: str,
                          original_price: str,
                          condition: str,
                          category: str,
                          delivery_options: str,
                          url: str,
                          payments_methods: str,
                          discounted_price: str,
                          discounted: bool,
                          seller_contact: str):
    async with main_session() as session:
        await session.execute(insert(MyProduct).values(
            photo=photo,
            brand=brand,
            price_range=price_range,
            currency=currency,
            channel_name=channel_name,
            title=title,
            size=size,
            description=description,
            original_price=original_price,
            condition=condition,
            category=category,
            delivery_options=delivery_options,
            url=url,
            payment_methods=payments_methods,
            discounted_price=discounted_price,
            discounted=discounted,
            seller_contact=seller_contact
        ))
        # await session.execute(insert(MyImage).values(data=photo, product_id=3))
        await session.commit()
