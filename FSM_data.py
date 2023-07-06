from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage


# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage: MemoryStorage = MemoryStorage()


# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSM_on(StatesGroup):
    cancel_call = State()
    continue_call = State()
    send_location = State()
    send_phone = State()
    send_gender = State()
    fill_FIO = State()
    fill_info = State()
    choose_age = State()
    wait_amb = State()
