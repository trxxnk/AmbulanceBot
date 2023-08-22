import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

from FSM.GetDataFSM import storage

from lexicon.lexicon_ru import MAIN_MENU

from handlers import bot_command_handlers, user_call_handlers


async def main():
    # Принимаем настройки
    config_path = None
    config: Config = load_config(config_path)

    # Иницициализация бота, диспетчера
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    # Регистрируем роутеры из handlers
    dp.include_routers(
        bot_command_handlers.router,
        user_call_handlers.router)

    # Устанавливаем "Меню" бота
    await bot.set_my_commands(MAIN_MENU)

    # [Временно] Пропускаем накопившиеся апдейты
    await bot.delete_webhook(drop_pending_updates=True)

    # Запускаем обработку апдейтов
    await dp.start_polling(bot)


asyncio.run(main())
