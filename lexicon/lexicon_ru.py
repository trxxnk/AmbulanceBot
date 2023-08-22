from aiogram.types import BotCommand


class BotCommands:
    def _getWithPrefix(command: str):
        prefix: str = '/'
        return prefix + command

    START_CMD: str = 'start'
    START: BotCommand = BotCommand(command=_getWithPrefix(START_CMD),
                                   description='Запуск/Перезапуск бота')

    HELP_CMD: str = 'help'
    HELP: BotCommand = BotCommand(command=_getWithPrefix(HELP_CMD),
                                  description='Что может этот бот')

    CANCEL_CALL_CMD: str = 'cancel_call'
    CANCEL_CALL: BotCommand = BotCommand(command=_getWithPrefix(CANCEL_CALL_CMD),
                                         description='Отменить вызов')


MAIN_MENU: list[BotCommand] = [
    BotCommands.START,
    BotCommands.HELP,
    BotCommands.CANCEL_CALL
]


class BotCommandsRU:
    START: str = '*ТЕКСТ НА* /start'  # TODO
    HELP: str = '*ТЕКСТ НА*  /help'  # TODO
    CANCEL_CALL: str = '*ТЕКСТ НА* /cancel_call'  # TODO


class PromtRU:
    CALL_AMB_BT: str = 'Вызвать скорую!'

    LOCATION_BT: str = ('Отправить геолокацию')
    LOCATION: str = ('Отправь мне своё местоположение, '
                     f'нажав на кнопку <b>{LOCATION_BT}</b>.')

    PHONE_BT: str = 'Отправить номер'
    PHONE: str = ('Для поддержки связи необходим номер телефона. '
                  f'Нажми на кнопку <b>{PHONE_BT}</b>.')

    INFO: str = ('Опишите тезисно о случившемся, '
                 'состоянии пострадавшего, жалобах больного.')

    FULL_NAME_BT: str = 'ФИО неизвестно'
    FULL_NAME: str = ('Отправь мне <b>"Фамилию Имя Отчество"</b> пострадвашего.'
                      f'Нажмите на кнопку {FULL_NAME_BT}, если не знаете.')

    # текст кнопок пола в GendersRU
    GENDER: str = ('Выберите <b>пол</b> больного кнопкой ниже.')

    # текст кнопок возраста в AgesRU и AgesRU_dict
    AGE: str = ('Выберите примерный возраст пострадавшего '
                '<b>кнопкой ниже</b> или отправьте <b>точный возраст</b> '
                'через клавиатуру.')

    WAIT_AMB: str = ('Данные успешно получены!\n'
                     'Скорая помощь уже в пути!')

    CANCEL_CALL_BT: str = 'Отменить вызов'
    CANCEL_CALL: str = ('Вы действительно хотите '
                        '<b>отменить</b> вызов?')
    YES_BT: str = 'Да'
    NO_BT: str = 'Нет'
    ABORT_CALL: str = 'Вы успешно отменили вызов.'

    DEFAULT_ANS: str = 'Некорректные данные. Повторите попытку!'

    UNKOWN_BT: str = 'Неизвестно'
    UNKOWN: str = 'Неизвестно'


class IgnoreRU:
    HELP: str = 'Пожалуйста, продолжите заполнение данных для вызова!.'
    START: str = 'На данном этапе нельзя запустить/перезапустить бота.'
    CANCEL_CALL: str = 'Вы еще не сделали вызов.'


class GendersRU:
    MAN: str = 'Мужской'
    WOMEN: str = 'Женский'
    UNKOWN: str = 'Неизвестно'

    GendersRU_dict: dict[str:str] = {
        'MAN': 'Мужской',
        'WOMEN': 'Женский',
        'UNKOWN': 'Неизветсно'
    }


class AgesRU:
    BABY: str = 'Младенец (до 1 года)'
    CHILD: str = 'Ребенок (1 - 13 лет)'
    TEEN: str = 'Подросток (14 - 17 лет)'
    YOUTH: str = 'Юношеский (18 - 24 года)'
    MIDDLE: str = 'Средний (45 - 59 лет)'
    ELDERY: str = 'Пожилой (60 - 74 года)'
    OLD: str = 'Страческий (Более 75 лeт)'
    UNKOWN: str = 'Неизвестно'

    AgesRU_dict: dict[str, str] = {
        'BABY':  'Младенец (до 1 года)',
        'CHILD':  'Ребенок (1 - 13 лет)',
        'TEEN':  'Подросток (14 - 17 лет)',
        'YOUTH':  'Юношеский (18 - 24 года)',
        'MIDDLE':  'Средний (45 - 59 лет)',
        'ELDERY':  'Пожилой (60 - 74 года)',
        'OLD':  'Страческий (Более 75 лeт)',
        'UNKOWN':  'Неизвестно'
    }
