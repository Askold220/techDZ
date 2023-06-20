import logging
import asyncio
import aiomysql
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

bot = Bot(token="token")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Параметри підключення до бази даних
db_config = {
    "host": "your_database_host",
    "user": "your_database_user",
    "password": "your_database_password",
    "db": "your_database_name",
    "autocommit": True,
}


async def get_products():
    conn = await aiomysql.connect(**db_config)
    cursor = await conn.cursor()
    await cursor.execute("SELECT * FROM product")  
    result = await cursor.fetchall()
    await cursor.close()
    conn.close()
    return result


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    tables = ['Таблиця 1', 'Таблиця 2', 'Таблиця 3']  # Список таблиць
    response = "Привіт! Ось список таблиць:\n" + "\n".join(tables)
    await message.reply(response)


@dp.message_handler(commands=['products'])
async def show_products(message: types.Message):
    products = await get_products()
    response = "Список товарів:\n\n"
    for product in products:
        response += f"Назва: {product[0]}\nЦіна: {product[1]}\n\n"
    await message.reply(response)


async def startup(dp):
    await bot.send_message(chat_id=chat_id, text='Бот запущено')


async def shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    from aiogram import executor
    loop = asyncio.get_event_loop()
    loop.create_task(startup(dp))
    try:
        executor.start_polling(dp, on_shutdown=shutdown)
        loop.run_forever()
    finally:
        loop.close()
