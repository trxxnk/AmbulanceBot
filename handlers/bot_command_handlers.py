from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter, Text, or_f
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from FSM.GetDataFSM import GetDataFSM  # [не используется] для работы с FSM
from promotions import PROMTS, IGNORE  # классы для отправки сообщений
from lexicon.lexicon_ru import BotCommands, BotCommandsRU, PromtRU  # текст сообщений


router: Router = Router()


# === /start ===
@router.message(Command(commands=[BotCommands.START_CMD]),
                StateFilter(default_state))
async def process_start_command(message: Message, state: FSMContext):
    await PROMTS.START.sendPromt(message)


@router.message(Command(commands=[BotCommands.START_CMD]),
                ~StateFilter(default_state))
async def ignore_start_command(message: Message, state: FSMContext):
    await IGNORE.START.sendPromt(message)
    await GetDataFSM.process_cur_step(update=message, state=state)
#  === /// ===


# === /help ===
@router.message(Command(commands=[BotCommands.HELP_CMD]),
                StateFilter(default_state))
async def process_help_command(message: Message, state: FSMContext):
    await PROMTS.HELP.sendPromt(message)


@router.message(Command(commands=[BotCommands.HELP_CMD]),
                ~StateFilter(default_state))
async def ignore_help_command(message: Message, state: FSMContext):
    await IGNORE.HELP.sendPromt(message)
    await GetDataFSM.process_cur_step(update=message, state=state)
# === /// ===


# === /cancel_call ===
@router.message(or_f(Command(commands=[BotCommands.CANCEL_CALL_CMD]),
                     Text(text=PromtRU.CANCEL_CALL_BT)),
                ~StateFilter(GetDataFSM.CANCEL_CALL),
                ~StateFilter(default_state))
async def process_cancel_call_command(message: Message, state: FSMContext):
    await state.update_data(state=await state.get_state())
    await state.set_state(GetDataFSM.CANCEL_CALL)
    await PROMTS.CANCEL_CALL.sendPromt(message)


@router.message(or_f(Command(commands=[BotCommands.CANCEL_CALL_CMD]),
                     Text(text=PromtRU.CANCEL_CALL_BT)))
async def ignore_cancel_call_command(message: Message, state: FSMContext):
    await IGNORE.CANCEL_CALL.sendPromt(message)
    await GetDataFSM.process_cur_step(update=message, state=state)
# === /// ===