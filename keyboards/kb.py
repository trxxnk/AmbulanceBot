from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import PromtRU


# === Кнопка&Клавиатура <Вызвать скорую!> ===
call_amb_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
CALL_AMB_BT: KeyboardButton = KeyboardButton(text=PromtRU.CALL_AMB_BT)
call_amb_kb_builder.row(CALL_AMB_BT, width=1)
CALL_AMB_KB: ReplyKeyboardMarkup = call_amb_kb_builder.as_markup(
    resize_keyboard=True)
# === /// ===


# === Кнопка&Клавиатура <Отменить вызов> ===
CANCEL_CALL_BT: KeyboardButton = KeyboardButton(
    text=PromtRU.CANCEL_CALL_BT)
cancel_call_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
cancel_call_kb_builder.row(CANCEL_CALL_BT, width=1)
CANCEL_CALL_KB: ReplyKeyboardMarkup = cancel_call_kb_builder.as_markup(
    resize_keyboard=True)
# === /// ===


# === Кнопка&Клавиатура <Отправить геолокацию> ===
LOCATION_BT: KeyboardButton = KeyboardButton(
    text=PromtRU.LOCATION_BT,
    request_location=True)
location_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
location_kb_builder.row(LOCATION_BT, CANCEL_CALL_BT, width=1)
LOCATION_KB: ReplyKeyboardMarkup = location_kb_builder.as_markup(
    resize_keyboard=True)
# === /// ===


# === Кнопка&Клавиатура <Отправить номер> ===
PHONE_BT: KeyboardButton = KeyboardButton(
    text=PromtRU.PHONE_BT,
    request_contact=True)
phone_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
phone_kb_builder.row(PHONE_BT, CANCEL_CALL_BT, width=1)
PHONE_KB: ReplyKeyboardMarkup = phone_kb_builder.as_markup(
    resize_keyboard=True)
# === /// ===


# === Кнопка/Клавиатура <Неизветсно>
UNKOWN_BT: KeyboardButton = KeyboardButton(
    text=PromtRU.UNKOWN_BT)
unkown_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
unkown_kb_builder.row(UNKOWN_BT, CANCEL_CALL_BT, width=1)
UNKOWN_KB: ReplyKeyboardMarkup = unkown_kb_builder.as_markup(
    resize_keyboard=True)
# === /// ===
