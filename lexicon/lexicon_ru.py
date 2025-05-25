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
                                  description='Что может этот бот?')

    CALL_AMB_CMD: str = 'call_amb'
    CALL_AMB: BotCommand = BotCommand(command=_getWithPrefix(CALL_AMB_CMD),
                                      description='Вызвать скорую')

    CANCEL_CALL_CMD: str = 'cancel_call'
    CANCEL_CALL: BotCommand = BotCommand(command=_getWithPrefix(CANCEL_CALL_CMD),
                                         description='Отменить вызов')
    
    ABOUT_CMD: str = 'about'
    ABOUT: BotCommand = BotCommand(command=_getWithPrefix(ABOUT_CMD),
                                   description='Информация о проекте')


MAIN_MENU: list[BotCommand] = [
    BotCommands.START,
    BotCommands.HELP,
    BotCommands.CALL_AMB,
    BotCommands.CANCEL_CALL,
    BotCommands.ABOUT
]

PRIMER_NOTE: str = ('<i>Примечание: Это учебный проект, не связанный '
               'с действующими службами спасения.</i>')

class BotCommandsRU:
    START: str = ('Привет! Я <u>учебный бот</u> для вызова скорой помощи. '
                  'Нажмите кнопку <a href="/call_amb">«Вызвать скорую»</a> '
                  '(или отправьте команду /call_amb) чтобы начать.\n\n'
                  + PRIMER_NOTE)    
    HELP: str = ('Я помогу вам вызвать скорую помощь. '
                 'Для этого нужно будет указать:\n'
                 '• Местоположение\n'
                 '• Контактный телефон\n'
                 '• Пол пострадавшего\n'
                 '• ФИО\n'
                 '• Информацию о случившемся\n'
                 '• Возраст\n\n'
                 'Нажмите кнопку <a href="/call_amb">«Вызвать скорую»</a> '
                 '(или отправьте команду /call_amb) чтобы начать.\n\n'
                 + PRIMER_NOTE)
    CANCEL_CALL: str = ('Вызов скорой помощи отменен. '
                       'Если вам снова потребуется помощь, '
                       'нажмите кнопку <a href="/call_amb">«Вызвать скорую»</a> '
                       '(или отправьте команду /call_amb).\n\n'
                       + PRIMER_NOTE)
    
    ABOUT: str = ('Этот бот создан в учебных целях для демонстрации работы с Telegram Bot API ' 
                  'на <code>Python</code> при помощи библиотеки <code>aiogram</code>.\n\n'
                  'На текущий момент планируется внедрение базы данных для хранения данных '
                  'о поступившем вызове, а также настройка <code>docker</code> проекта для запуска бота.\n\n'
                  '• <b>Bot username:</b> @dev_ambulance_bot \n'
                  '• <b>Developer:</b> @trxxnk \n'
                  '• <b>GitHub:</b> https://github.com/trxxnk/AmbulanceBot \n\n'
                  + PRIMER_NOTE)


class PromtRU:
    CALL_AMB_BT: str = 'Вызвать скорую!'

    LOCATION_BT: str = ('Отправить геолокацию')
    LOCATION: str = ('Отправьте мне своё местоположение, '
                     f'нажав на кнопку «<b>{LOCATION_BT}</b>».')

    PHONE_BT: str = 'Отправить номер'
    PHONE: str = ('Для поддержки связи необходим номер телефона. '
                  f'Нажмите на кнопку «<b>{PHONE_BT}</b>».')

    INFO: str = ('Опишите тезисно о случившемся, '
                 'состоянии пострадавшего, жалобах больного.')

    FULL_NAME_BT: str = 'ФИО неизвестно'
    FULL_NAME: str = ('Отправьте мне <b>"Фамилию Имя Отчество"</b> пострадвашего. '
                      f'Нажмите на кнопку «<b>{FULL_NAME_BT}</b>», если не знаете.')

    # текст кнопок пола в GendersRU
    GENDER: str = ('Выберите <b>пол</b> больного кнопкой ниже.')

    # текст кнопок возраста в AgesRU и AgesRU_dict
    AGE: str = ('Выберите примерный возраст пострадавшего '
                '<b>кнопкой ниже</b> или отправьте <b>точный возраст</b> '
                'через клавиатуру при помощи ввода цифр.')

    WAIT_AMB: str = ('Данные успешно получены!\n'
                     'Скорая помощь уже в пути!\n\n'
                     '(Скоро процесс "ожидания скорой помощи" будет завершен, '
                     'бот вернется в исходное состояние готовности к новому вызову)\n\n'
                     + PRIMER_NOTE)
    WAIT_AMB_END: str = ('Скорая помощь прибыла!\n'
                         'Сейчас вы можете продолжить заполнение данных '
                         'для нового вызова.\n\n'
                         + PRIMER_NOTE)

    CANCEL_CALL_BT: str = 'Отменить вызов'
    CANCEL_CALL: str = ('Вы действительно хотите '
                        '<b>отменить</b> вызов?')
    YES_BT: str = 'Да'
    NO_BT: str = 'Нет'
    ABORT_CALL: str = 'Вы успешно отменили вызов.'

    DEFAULT_ANS: str = 'Некорректный ввод. Повторите попытку!'

    UNKOWN_BT: str = 'Неизвестно'
    UNKOWN: str = 'Неизвестно'


class IgnoreRU:
    HELP: str = 'Пожалуйста, продолжите заполнение данных для вызова!'
    START: str = 'На данном этапе нельзя запустить/перезапустить бота.'
    CALL_AMB: str = 'Вы уже сделали вызов.'
    CANCEL_CALL: str = 'Вы еще не сделали вызов.'
    ABOUT: str = 'Отмените вызов или завершите ввод данных для получения информации о проекте.'

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
