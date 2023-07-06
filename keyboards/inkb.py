from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU, AGES_RU


# === Неизвестно ===
buttons = [
    [InlineKeyboardButton(
        text=LEXICON_RU['unkown'],
        callback_data='unkown_pressed')]
]

unkown_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=buttons
)
# === /// ===


# === Выбрать пол ===
choose_sex_kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
buttons: list[InlineKeyboardButton] = [
    InlineKeyboardButton(
        text=LEXICON_RU['man_gender'],
        callback_data='man'),
    InlineKeyboardButton(
        text=LEXICON_RU['women_gender'],
        callback_data='women'),
    InlineKeyboardButton(
        text=LEXICON_RU['unkown'],
        callback_data='unkown_pressed'),
]
choose_sex_kb_builder.row(*buttons, width=2)
choose_sex_kb: InlineKeyboardMarkup = choose_sex_kb_builder.as_markup()


# === Выбрать возраст ===
buttons: list[InlineKeyboardButton] = [
    [InlineKeyboardButton(
        text=txt,
        callback_data=cb_data)] for cb_data, txt in AGES_RU._asdict().items()
]

choose_age_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=buttons
)
# === /// ===

# === Да / Нет для отмены вызова ===
buttons: list[list[InlineKeyboardButton]] = [
    [InlineKeyboardButton(
        text=LEXICON_RU['yes'],
        callback_data='yes_cancel')],
    [InlineKeyboardButton(
        text=LEXICON_RU['no'],
        callback_data='no_cancel')]
]

yes_no_inkb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=buttons)
# === /// ===

# === Продолжить вызов / заполнение данных ===
buttons: list[list[InlineKeyboardButton]] = [
    [InlineKeyboardButton(
        text=LEXICON_RU['continue'],
        callback_data='continue_call')],
]
continue_inkb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=buttons
)
# === /// ===
