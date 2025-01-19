from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import (
    Integer,
    Text,
    String,
    PrimaryKeyConstraint,
)


class Base(DeclarativeBase):
    pass


# class User(Base):
#     __tablename__ = "users"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     tg_id: Mapped[int] = mapped_column(BigInteger)
#     email: Mapped[str] = mapped_column(Text)
#     username: Mapped[str] = mapped_column(String(50))
#     password: Mapped[str] = mapped_column(Text)
#     _is_admin: Mapped[str] = mapped_column(Text)


# class TGProduct(Base):
#     __tablename__ = "telegram_products"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     url: Mapped[str] = mapped_column(Text)


# class Category(Base):
#     __tablename__ = 'categories'


# class Yep(Base):
#     __tablename__ = 'yep'
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     caption: Mapped[str] = mapped_column(Text)
#     photo: Mapped[str] = mapped_column(Text, default='No_photo')


# class Product(Base):
#     __tablename__ = "products"
#
#     id: Mapped[int] = mapped_column(Integer)
#     type: # Mapped[str] = mapped_column(Text)
#     title: Mapped[str] = mapped_column(Text, default='No title')
#     image: Mapped[str] = mapped_column(Text, default='No image')
#     size: Mapped[str] = mapped_column(String(40), default='No size')
#     description: Mapped[str] = mapped_column(Text, default='No description')
#     is_used: Mapped[str] = mapped_column(String(50), nullable=False)
#     target_audience: Mapped[str] = mapped_column(Text)
#     price: Mapped[float] = mapped_column(Float, nullable=False)
#     created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
#
#     __table_args__ = (
#         CheckConstraint('price >= 0', "Good price"),
#         PrimaryKeyConstraint('id', 'type', name='Unique product')
#     )
# CheckConstraint('price >= 0', "Good price"),

class MyProduct(Base):
    __tablename__ = "my_products"

    product_id: Mapped[int] = mapped_column(Integer)
    source: Mapped[str] = mapped_column(String(100), nullable=False)
    title: Mapped[str] = mapped_column(Text, server_default='No title')
    size: Mapped[str] = mapped_column(Text, server_default='No size')
    description: Mapped[str] = mapped_column(Text, server_default='No description')
    price: Mapped[str] = mapped_column(Text, nullable=False)
    state: Mapped[str] = mapped_column(Text, nullable=False)
    available: Mapped[str] = mapped_column(String(50), server_default='Is available')
    image: Mapped[str] = mapped_column(Text, default='No image')

    # image: Mapped['MyImage'] = relationship('MyImage', back_populates='product', uselist=False)

    __table_args__ = (
        PrimaryKeyConstraint('product_id', name='Unique my_product'),
    )


# class MyImage(Base):
    # __tablename__ = "images"
    #
    # image_id: Mapped[int] = mapped_column(Integer)
    # data: Mapped[str] = mapped_column(Text, nullable=False)
    # product_id: Mapped[int] = mapped_column(ForeignKey('my_products.product_id', ondelete='CASCADE'), nullable=False)
    #
    # product: Mapped['MyProduct'] = relationship('MyProduct', back_populates='image', uselist=False)
    #
    # __table_args__ = (
    #     PrimaryKeyConstraint('image_id', name="Unique image"),
    # )
