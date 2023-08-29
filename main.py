from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_BOT


HELP_COMMAND = """
/start - начало работы с ботом
/help - список команд
/description - описание бота
"""

DESCRIPTION_OF_BOT = """
octaviusAYVKBot - Телеграмм-бот, который поможет тебе в решении большого количества задач.
Теперь ты не сможешь сказать, что у тебя не сто рук)
"""

CALLING_COUNT = 0

bot = Bot(TOKEN_BOT)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Добро пожаловать на наш Телеграмм-канал')
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text=DESCRIPTION_OF_BOT)
    await message.delete()


@dp.message_handler()
async def hello_echo(message: types.Message):
    if message.text.lower() in ['hello', 'hello.', 'hello!', 'hi',
                                'привет', 'привет.', 'привет!',
                                'добрый день', 'добрый день.', 'добрый день!']:
        await message.answer(text=message.text)


if __name__ == "__main__":
    executor.start_polling(dp)
