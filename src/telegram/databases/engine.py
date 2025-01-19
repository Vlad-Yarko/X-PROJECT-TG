from dotenv import load_dotenv, find_dotenv

import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


load_dotenv(find_dotenv())

engine = create_async_engine(url=os.getenv('DB'))
main_session = async_sessionmaker(bind=engine, class_=AsyncSession)
