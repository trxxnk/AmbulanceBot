from aiogram import Router, F

from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from FSM_data import FSM_on

from DB import USERS, User

from lexicon.lexicon_ru import LEXICON_RU, AGES_RU

from aiogram.types import InlineKeyboardMarkup
from keyboards.kb import (geolocation_kb, contact_kb,
                          yes_no_kb, call_amb_kb,
                          unkown_kb, cancel_call_kb)
from keyboards.inkb import (choose_sex_kb,
                            choose_age_kb, continue_inkb,
                            yes_no_inkb)

router: Router = Router()


# === Вызвать скорую! ===
@router.message(Text(text=LEXICON_RU['call_amb']))
async def process_call_amb_text(message: Message, state: FSMContext):
    # заменить на обращение к БД
    USERS[message.from_user.id] = User(id=message.from_user.id,
                                       time=message.date)
    await message.answer(
        text=LEXICON_RU['get_location'],
        reply_markup=geolocation_kb
    )
    USERS[message.from_user.id].step['state'] = FSM_on.send_location
    USERS[message.from_user.id].step['func'] = process_no_location_data
    await state.set_state(FSM_on.send_location)
# === /// ===


# === Отмена вызова ===
# --- Подтверждение отмены ---
@router.callback_query(StateFilter(FSM_on.cancel_call),
                       Text(text=['yes_cancel']))
async def process_yes_cancel(callback: CallbackQuery, state: FSMContext):
    delete_user = USERS.pop(callback.from_user.id, None)
    await callback.message.edit_text(
        text=LEXICON_RU['yes_cancel'],
        reply_markup=None)
    await callback.message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=call_amb_kb
    )


# --- Отмена отмены ---
@router.callback_query(StateFilter(FSM_on.cancel_call),
                       Text(text=['no_cancel']))
async def process_yes_cancel(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=LEXICON_RU['no_cancel'],
        reply_markup=continue_inkb)
    await state.set_state(FSM_on.continue_call)


@router.message(StateFilter(FSM_on.cancel_call))
async def process_default(message: Message, state: FSMContext):
    await message.reply(
        text=LEXICON_RU['/cancel'],
        reply_markup=yes_no_inkb,
    )
# === /// ===


# === Продолжить вызов ===
@router.callback_query(StateFilter(FSM_on.continue_call), Text(text=['continue_call']))
async def process_continue_pressed(callback: CallbackQuery, state: FSMContext):
    await state.set_state(USERS[callback.from_user.id].step['state'])
    await USERS[callback.from_user.id].step['func'](
        message=callback.message,
        state=state)
    await callback.message.delete()


# --- Проигнорирована кнопка "Продолжить" ---
@router.message(StateFilter(FSM_on.continue_call))
async def process_no_continue_pressed(message: CallbackQuery, state: FSMContext):
    await message.answer(
        text=LEXICON_RU['no_cancel'],
        reply_markup=continue_inkb
    )
# === /// ===


# === Отправить геолокацию ===
@router.message(F.content_type == ContentType.LOCATION, StateFilter(FSM_on.send_location))
async def process_location_data(message: Message, state: FSMContext):
    latitude: float = message.location.latitude
    longitude: float = message.location.longitude
    USERS[message.from_user.id].location = (latitude, longitude)
    await message.answer(
        text=LEXICON_RU['get_phone'],
        reply_markup=contact_kb)
    USERS[message.from_user.id].step['state'] = FSM_on.send_phone
    USERS[message.from_user.id].step['func'] = process_no_contact_data
    await state.set_state(FSM_on.send_phone)


# --- Некорректные данные о локации ---
@router.message(StateFilter(FSM_on.send_location))
async def process_no_location_data(message: Message, state: FSMContext):
    await message.reply(
        text=LEXICON_RU['incorrect_location'],
        reply_markup=geolocation_kb)
#  === /// ===


# === Отправить контакт ===
@router.message(F.content_type == ContentType.CONTACT, StateFilter(FSM_on.send_phone))
async def process_contact_data(message: Message, state: FSMContext):
    user_phone = message.contact.phone_number
    USERS[message.from_user.id].phone = user_phone
    await message.answer(
        text=LEXICON_RU['get_info'],
        reply_markup=cancel_call_kb
    )
    USERS[message.from_user.id].step['state'] = FSM_on.fill_info
    USERS[message.from_user.id].step['func'] = process_no_fill_info
    await state.set_state(FSM_on.fill_info)


@router.message(StateFilter(FSM_on.send_phone))
async def process_no_contact_data(message: Message, state: FSMContext):
    await message.reply(
        text=LEXICON_RU['get_phone'],
        reply_markup=contact_kb)
# === /// ===


# === Отправка информации о случившемся ===
@router.message(StateFilter(FSM_on.fill_info),
                F.content_type == ContentType.TEXT)
async def process_fill_info(message: Message, state: FSMContext):
    USERS[message.from_user.id].info = message.text
    USERS[message.from_user.id].step['state'] = FSM_on.fill_FIO
    USERS[message.from_user.id].step['func'] = process_no_fill_FIO
    await state.set_state(FSM_on.fill_FIO)
    await message.answer(
        text=LEXICON_RU['get_FIO'],
        reply_markup=unkown_kb
    )


@router.message(StateFilter(FSM_on.fill_info), ~F.content_type == ContentType.TEXT,)
async def process_no_fill_info(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON_RU['get_info'],
        reply_markup=cancel_call_kb
    )
# === /// ===


# === Отправка ФИО ===
# --- ФИО неизвестно ---
@ router.message(StateFilter(FSM_on.fill_FIO),
                 Text(text=[LEXICON_RU['unkown']]))
async def callback_unkown_FIO(message: CallbackQuery, state: FSMContext):
    # TODO: БД
    USERS[message.from_user.id].FIO = message.text
    USERS[message.from_user.id].step['state'] = FSM_on.send_gender
    USERS[message.from_user.id].step['func'] = callback_no_choose_gender
    await state.set_state(FSM_on.send_gender)
    await message.answer(
        text=LEXICON_RU['get_gender'],
        reply_markup=choose_sex_kb
    )


@router.message(StateFilter(FSM_on.fill_FIO),
                F.content_type == ContentType.TEXT,
                # !!! фильтр-парсер ФИО !!!
                )
async def process_fill_FIO(message: Message, state: FSMContext):
    # TODO: БД
    USERS[message.from_user.id].FIO = message.text
    USERS[message.from_user.id].step['state'] = FSM_on.send_gender
    USERS[message.from_user.id].step['func'] = callback_no_choose_gender
    await message.answer(
        text=LEXICON_RU['get_gender'],
        reply_markup=choose_sex_kb
    )
    await state.set_state(FSM_on.send_gender)


# --- Некорректное ФИО ---
@ router.message(StateFilter(FSM_on.fill_FIO))
async def process_no_fill_FIO(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON_RU['get_FIO'],
        reply_markup=unkown_kb)


# === /// ===


# === Выбрать пол ===
@ router.callback_query(StateFilter(FSM_on.send_gender),
                        Text(text=['man', 'women', 'unkown_pressed']))
async def callback_choose_gender(callback: CallbackQuery, state: FSMContext):
    # TODO: БД
    USERS[callback.from_user.id].gender = callback.data
    USERS[callback.from_user.id].step['state'] = FSM_on.choose_age
    USERS[callback.from_user.id].step['func'] = callback_no_choose_age
    await callback.message.edit_text(
        text=LEXICON_RU['get_age'],
        reply_markup=choose_age_kb)
    await state.set_state(FSM_on.choose_age)


# --- Некорректный ввод пола ---
@ router.callback_query(StateFilter(FSM_on.send_gender))
async def callback_no_choose_gender(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON_RU['get_gender'],
        reply_markup=choose_sex_kb)
# === /// ===


# === Выбрать возраст ===
@ router.callback_query(Text(text=AGES_RU._fields),
                        StateFilter(FSM_on.choose_age))
async def callback_choose_age(callback: CallbackQuery, state: FSMContext):
    # TODO: БД
    USERS[callback.from_user.id].age = callback.data
    USERS[callback.from_user.id].step['state'] = FSM_on.wait_amb
    USERS[callback.from_user.id].step['func'] = process_wait_amb
    await callback.message.edit_text(
        text=LEXICON_RU['data_complete'],
    )
    await state.set_state(FSM_on.wait_amb)


# --- Некорректный ввод возраста ---
async def callback_no_choose_age(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON_RU['get_age'],
        reply_markup=choose_age_kb
    )


# --- Возраст отправлен числом ---
@ router.message(StateFilter(FSM_on.choose_age), Text(contains=['1234567890']))
async def process_number_choose_age(message: Message, state: FSMContext):
    # TODO: БД
    USERS[message.from_user.id] = message.text
    state.set_state(FSM_on.wait_amb)
    USERS[message.from_user.id].step['step'] = FSM_on.wait_amb
    USERS[message.from_user.id].step['func'] = process_wait_amb
    await process_wait_amb(message=message, state=state)
# === /// ===


# === Ожидание приезда скорой ===
@ router.message(StateFilter(FSM_on.wait_amb))
async def process_wait_amb(message: Message, state: FSMContext):
    await message.reply(
        text=LEXICON_RU['wait_amb'],
        reply_markup=cancel_call_kb
    )
# === /// ===


# === Удаление старых сообщений с инлайн кнопками, если они будут нажаты ===
@router.callback_query()
async def delete_old_message(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
# === /// ===
