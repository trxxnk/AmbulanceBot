import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

from FSM_data import storage


from handlers import bot_command_handlers, user_handlers, callback_handlers
from keyboards.set_menu import set_main_menu


async def main():
    # Принимаем настройки
    config_path = None
    config: Config = load_config(config_path)

    # Иницициализация бота, диспетчера
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML'
              )

    dp = Dispatcher(storage=storage)

    # Регистрируем роутеры из handlers
    dp.include_routers(
        bot_command_handlers.router,
        user_handlers.router,
        callback_handlers.router
    )

    # Настраиваем кнопку Menu
    await set_main_menu(bot)

    # (???) Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
