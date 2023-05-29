import logging
from datetime import datetime as dt

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils import config
from manager_handlers import handlers


storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=config.BOT_TOKEN)

# Диспетчер
dp = Dispatcher(bot=bot, storage=storage)

# Регистрация хэндлеров
dp.register_message_handler(callback=handlers.send_welcome, commands=['start', 'help'])

dp.register_message_handler(callback=handlers.random_plant, commands=['plant'])

dp.register_message_handler(callback=handlers.joker, commands=['joke'])

dp.register_message_handler(callback=handlers.recommendation, commands=['advice'])

dp.register_message_handler(callback=handlers.weather_data, commands=['weather'])

dp.register_message_handler(callback=handlers.orange_tree, commands=['orange'])


if __name__ == '__main__':
    print(f'Бот запущен, текущее время: {dt.now()}')
    executor.start_polling(dp, skip_updates=True)
    print(f'Бот приостановлен, текущее время: {dt.now()}')
