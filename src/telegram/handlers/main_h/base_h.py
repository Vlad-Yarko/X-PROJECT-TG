from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.telegram.fsm.chanels import Chanel


base_command_router = Router()
base_command_router.message.filter(StateFilter(None))
base_command_router.callback_query.filter(StateFilter(None))

quit_store_router = Router()
quit_store_router.message.filter(StateFilter(Chanel))


@base_command_router.message(Command('start'))
async def start_bot(message: Message):
    await message.answer('What would you like to do?')


@base_command_router.message(Command('zyscel'))
async def zyscel_store_start(message: Message, state: FSMContext):
    await state.set_state(Chanel.active_zyscel)
    await message.answer('Give your products')


@base_command_router.message(Command('keshkatura'))
async def keshkature_store_start(message: Message, state: FSMContext):
    await state.set_state(Chanel.active_keshtatura)
    await message.answer('Give your products')


@base_command_router.message(Command('casual_italy'))
async def keshkature_store_start(message: Message, state: FSMContext):
    await state.set_state(Chanel.active_casual_italy)
    await message.answer('Give your products')


@quit_store_router.message(Command('quit'))
async def quit_chanel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('You returned in menu')
