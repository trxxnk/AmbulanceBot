from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import PromtRU, GendersRU, AgesRU
from .callback_data import CancelCallCB

# === Клавиатура <Выбрать пол> ===
genders_inkb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
genders_buttons: list[InlineKeyboardButton] = [
    InlineKeyboardButton(callback_data=key, text=value)
    for key, value in GendersRU.GendersRU_dict.items()]
genders_inkb_builder.row(*genders_buttons, width=2)
GENDERS_INKB: InlineKeyboardMarkup = genders_inkb_builder.as_markup()


# === Клавиатура <Выбрать возраст> ===
ages_buttons: list[InlineKeyboardButton] = [
    [InlineKeyboardButton(callback_data=key, text=value)]
    for key, value in AgesRU.AgesRU_dict.items()]

AGES_INKB: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=ages_buttons)
# === /// ===


# === Клавиатура <Да/Нет> для отмены вызова ===
YES_CANCEL_CALL: InlineKeyboardButton = InlineKeyboardButton(
    text=PromtRU.YES_BT,
    callback_data=CancelCallCB.YES_CANCEL_CALL)
NO_CANCEL_CALL: InlineKeyboardButton = InlineKeyboardButton(
    text=PromtRU.NO_BT,
    callback_data=CancelCallCB.NO_CANCEL_CALL)
yes_no_inkb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
yes_no_inkb_builder.row(YES_CANCEL_CALL, NO_CANCEL_CALL, width=2)
YES_NO_INKB: InlineKeyboardMarkup = yes_no_inkb_builder.as_markup()
# === /// ===
