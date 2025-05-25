# TODO: Походу лучше переселить это все дело в FSM

from aiogram.types import (
    InlineKeyboardMarkup, ReplyKeyboardMarkup,
    ReplyKeyboardRemove, Message, CallbackQuery)

from dataclasses import dataclass
from typing import Union

from lexicon.lexicon_ru import PromtRU, BotCommandsRU, IgnoreRU
import keyboards.inkb as inkb
import keyboards.kb as kb


@dataclass
class Promt:
    text: str = 'no_promt_text'
    kb: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup,
              ReplyKeyboardRemove] = ReplyKeyboardRemove()

    async def sendPromt(self, update: Union[CallbackQuery, Message]):
        if isinstance(update, CallbackQuery):
            # [InlineKeyboardMarkup]
            if isinstance(self.kb, InlineKeyboardMarkup):
                await update.message.edit_text(
                    text=self.text,
                    reply_markup=self.kb)
            else:  # [ReplyKeyboardMarkup, ReplyKeyboardRemove]
                await update.message.delete()
                await update.message.answer(
                    text=self.text,
                    reply_markup=self.kb)

        elif isinstance(update, Message):
            await update.answer(
                text=self.text,
                reply_markup=self.kb,
                disable_web_page_preview=True)

    def __repr__(self):
        return f'Step(kb={self.kb}, text={self.text})'


class PROMTS:
    LOCATION: Promt = Promt(text=PromtRU.LOCATION, kb=kb.LOCATION_KB)
    PHONE: Promt = Promt(text=PromtRU.PHONE, kb=kb.PHONE_KB)
    AGE: Promt = Promt(text=PromtRU.AGE, kb=inkb.AGES_INKB)
    INFO: Promt = Promt(text=PromtRU.INFO, kb=kb.CANCEL_CALL_KB)
    FULL_NAME: Promt = Promt(text=PromtRU.FULL_NAME, kb=kb.UNKOWN_KB)
    GENDER: Promt = Promt(text=PromtRU.GENDER, kb=inkb.GENDERS_INKB)
    CANCEL_CALL: Promt = Promt(text=PromtRU.CANCEL_CALL, kb=inkb.YES_NO_INKB)

    WAIT_AMB: Promt = Promt(text=PromtRU.WAIT_AMB, kb=kb.CANCEL_CALL_KB)
    WAIT_AMB_END: Promt = Promt(text=PromtRU.WAIT_AMB_END, kb=kb.CALL_AMB_KB)

    START: Promt = Promt(text=BotCommandsRU.START, kb=kb.CALL_AMB_KB)
    HELP: Promt = Promt(text=BotCommandsRU.HELP, kb=kb.CALL_AMB_KB)
    ABOUT: Promt = Promt(text=BotCommandsRU.ABOUT, kb=kb.CALL_AMB_KB)

    DEFAULT_ANS: Promt = Promt(text=PromtRU.DEFAULT_ANS)


class IGNORE:
    START: Promt = Promt(text=IgnoreRU.START)
    HELP: Promt = Promt(text=IgnoreRU.HELP)
    CALL_AMB: Promt = Promt(text=IgnoreRU.CALL_AMB)
    CANCEL_CALL: Promt = Promt(text=IgnoreRU.CANCEL_CALL)
    ABOUT: Promt = Promt(text=IgnoreRU.ABOUT)
