from aiogram import Router

from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from FSM_data import FSM_on

from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, ReplyKeyboardRemove

from DB import USERS

from keyboards.kb import call_amb_kb
from keyboards.inkb import yes_no_inkb, continue_inkb

from lexicon.lexicon_ru import LEXICON_RU


router: Router = Router()


# === /start ===
@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=call_amb_kb)
#  === /// ===


# === /help ===
@router.message(Command(commands=['help']), StateFilter(default_state))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/help']
    )
# === /// ===


# === /cancel ===
@router.message(Text(text=[LEXICON_RU['cancel_call_kb'], '/cancel']),
                ~StateFilter(default_state),
                ~StateFilter(FSM_on.cancel_call))
async def process_cancel_command(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON_RU['/cancel'],
        reply_markup=yes_no_inkb,
    )
    await state.set_state(FSM_on.cancel_call)
# === /// ===
