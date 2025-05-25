from typing import Union

from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

from promotions import Promt, PROMTS

from dataclasses import dataclass

# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage: MemoryStorage = MemoryStorage()


@dataclass
class Step:
    state: State
    promt: Promt


# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class GetDataFSM(StatesGroup):

    NUM_STEP: dict[int:Step] = {
        -1: Step(state=(CANCEL_CALL := State(state='CANCEL_CALL', group_name='GetDataFSM')), promt=PROMTS.CANCEL_CALL),
        0: Step(state=default_state, promt=PROMTS.START),
        1: Step(state=(GET_LOCATION := State(state='GET_LOCATION', group_name='GetDataFSM')), promt=PROMTS.LOCATION),
        2: Step(state=(GET_PHONE := State(state='GET_PHONE', group_name='GetDataFSM')), promt=PROMTS.PHONE),
        3: Step(state=(GET_GENDER := State(state='GET_GENDER', group_name='GetDataFSM')), promt=PROMTS.GENDER),
        4: Step(state=(GET_FULL_NAME := State(state='GET_FULL_NAME', group_name='GetDataFSM')), promt=PROMTS.FULL_NAME),
        5: Step(state=(GET_INFO := State(state='GET_INFO', group_name='GetDataFSM')), promt=PROMTS.INFO),
        6: Step(state=(GET_AGE := State(state='GET_AGE', group_name='GetDataFSM')), promt=PROMTS.AGE),
        7: Step(state=(WAIT_AMB := State(state='WAIT_AMB', group_name='GetDataFSM')), promt=PROMTS.WAIT_AMB)
    }

    STATE_NUM: dict[State:int] = {
        step.state: num_step for num_step, step in NUM_STEP.items()}
    STATE_NUM[None] = 0

    @classmethod
    async def process_cur_step(cls, *, update: Union[Message, CallbackQuery], state: FSMContext) -> None:
        cur_state: Union[State, None] = await state.get_state()
        num_cur_step: int = GetDataFSM.STATE_NUM[cur_state]
        cur_step: Step = GetDataFSM.NUM_STEP[num_cur_step]
        # print(cur_step.promt)
        await cur_step.promt.sendPromt(update)

    @classmethod
    async def process_next_step(cls, *, update: Union[Message, CallbackQuery], state: FSMContext) -> None:
        cur_state: State = await state.get_state()
        # print(cur_state)
        num_next_step: int = GetDataFSM.STATE_NUM[cur_state] + 1
        next_step: Step = GetDataFSM.NUM_STEP[num_next_step]
        await state.set_state(next_step.state)
        await next_step.promt.sendPromt(update)
