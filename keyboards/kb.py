from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# === Вызвать скорую! ===
call_amb_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
buttons: list[KeyboardButton] = [
    KeyboardButton(text=LEXICON_RU['call_amb'])
]
call_amb_kb_builder.row(*buttons, width=1)
call_amb_kb: ReplyKeyboardMarkup = call_amb_kb_builder.as_markup(
    resize_keyboard=True
)
# === /// ===


# === Отменить вызов ===
cancel_bt: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['cancel_call_kb']
)

cancel_call_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[cancel_bt]],
    resize_keyboard=True
)
# === /// ===


# === Да / Нет для отмены вызова
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
buttons: KeyboardButton = [
    KeyboardButton(
        text=LEXICON_RU['yes']),
    KeyboardButton(
        text=LEXICON_RU['no'])
]
yes_no_kb_builder.row(*buttons, width=2)
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    resize_keyboard=True
)
# === /// ===


# === Кнопка "Неизвестно' ===
unkown_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(
            text=LEXICON_RU['unkown'],
        )],
        [cancel_bt]
    ],
    resize_keyboard=True
)
# === /// ===


# === Отправить местонахождение ===
geolocation_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
buttons: KeyboardButton = [
    KeyboardButton(
        text=LEXICON_RU['send_location_bt'],
        request_location=True),
    cancel_bt
]
geolocation_kb_builder.row(*buttons, width=1)
geolocation_kb: ReplyKeyboardMarkup = geolocation_kb_builder.as_markup(
    resize_keyboard=True)
# === /// ===


# === Отправить номер телефона ===
contact_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
buttons: KeyboardButton = [
    KeyboardButton(
        text=LEXICON_RU['send_phone_bt'],
        request_contact=True),
    cancel_bt
]
contact_kb_builder.row(*buttons, width=1)
contact_kb: ReplyKeyboardMarkup = contact_kb_builder.as_markup(
    resize_keyboard=True)
# === /// ===


# === Остальные клавиатуры ===
# === /// ===
