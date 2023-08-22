from aiogram import Router, F

from aiogram.filters import StateFilter, Text, Command
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State

from FSM.GetDataFSM import GetDataFSM
from DB import USERS, User
from lexicon.lexicon_ru import BotCommands, PromtRU, GendersRU, AgesRU
from promotions import PROMTS, IGNORE
from keyboards.callback_data import CancelCallCB

import time


router: Router = Router()


# Подтверждение отмены вызова
@router.callback_query(Text(text=CancelCallCB.YES_CANCEL_CALL),
                       StateFilter(GetDataFSM.CANCEL_CALL))
async def process_approve_cancel_call(callback: CallbackQuery, state: FSMContext):
    await state.set_state(default_state)
    await state.clear()
    await callback.message.edit_text(text=PromtRU.ABORT_CALL)
    await PROMTS.HELP.sendPromt(callback.message)


# Аборт отмены вызова
@router.callback_query(Text(text=CancelCallCB.NO_CANCEL_CALL),
                       StateFilter(GetDataFSM.CANCEL_CALL))
async def process_abort_cancel_call(callback: CallbackQuery, state: FSMContext):
    new_data: dict = await state.get_data()
    cur_state: State = new_data.pop('state', None)
    await state.set_state(cur_state)
    await GetDataFSM.process_cur_step(update=callback, state=state)


# <Вызвать скорую!>
@router.message(Text(text=PromtRU.CALL_AMB_BT))
async def process_call_amb(message: Message, state: FSMContext):
    await state.update_data(id=message.from_user.id, time=message.date, step=1)
    await GetDataFSM.process_next_step(update=message, state=state)


# Получение геолокации
@router.message(F.content_type.in_({ContentType.LOCATION}),
                StateFilter(GetDataFSM.GET_LOCATION))
async def process_get_location(message: Message, state: FSMContext):
    await state.update_data(location=message.location)
    await GetDataFSM.process_next_step(update=message, state=state)


# Получение телефона
@router.message(F.content_type.in_({ContentType.CONTACT}),
                StateFilter(GetDataFSM.GET_PHONE))
async def process_get_location(message: Message, state: FSMContext):
    await state.update_data(location=message.location)
    await GetDataFSM.process_next_step(update=message, state=state)


# Получение пола
@router.callback_query(Text(text=GendersRU.GendersRU_dict.keys()),
                       StateFilter(GetDataFSM.GET_GENDER))
async def process_get_gender(callback: CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data)
    await GetDataFSM.process_next_step(update=callback, state=state)


# Получение ФИО
@router.message(F.content_type == ContentType.TEXT,
                StateFilter(GetDataFSM.GET_FULL_NAME))
async def process_get_full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await GetDataFSM.process_next_step(update=message, state=state)


# Получение информаци о случившемся/ жалобах пострадавшего
@router.message(F.content_type == ContentType.TEXT,
                StateFilter(GetDataFSM.GET_INFO))
async def process_get_info(message: Message, state: FSMContext):
    await state.update_data(info=message.text)
    await GetDataFSM.process_next_step(update=message, state=state)


# Получение возраста
@router.callback_query(Text(text=AgesRU.AgesRU_dict.keys()),
                       StateFilter(GetDataFSM.GET_AGE))
async def process_get_age(callback: CallbackQuery, state: FSMContext):
    await state.update_data(age=callback.data)
    await GetDataFSM.process_next_step(update=callback, state=state)


# Ожидание скорой
@router.message(StateFilter(GetDataFSM.WAIT_AMB))
async def process_wait_amb(message: Message, state: FSMContext):
    await PROMTS.WAIT_AMB.sendPromt(message)
    # TODO: Какой-то флаг, что скорая приехала
    await message.answer(
        text='Типа скорая приехала')
    await state.set_state(default_state)
    await PROMTS.HELP.sendPromt(message)


# Дефолтный фильтр
@router.message()
async def process_default_filter(message: Message, state: FSMContext):
    await PROMTS.DEFAULT_ANS.sendPromt(message)
    await GetDataFSM.process_cur_step(update=message, state=state)
