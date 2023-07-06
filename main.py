"""
This is a echo bot.
It echoes any incoming text messages.
"""

from aiogram import Bot, Dispatcher, executor, types
import logging


API_TOKEN = "5902292713:AAGlOd3ZJnvxV6Cnd_niOF2JWdZnmVIouOE"
# Настройка вывода логов
logging.basicConfig(
    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]\
        %(message)s',
    level=logging.INFO  # что нужно логировать
)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        "Привет! Я бот скорой помощи.\nЕсли срочно нужна помощь, то нажми на кнопку SOS"
    )


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
