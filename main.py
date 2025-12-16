import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8367085105:AAFAHx9rUyIG-v7m6OxAFCOPuwlOpkZbZeI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

spisok = ["камень", "ножницы", "бумага"]

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Напиши: камень, ножницы или бумага")

@dp.message()
async def game(message: types.Message):
    user_choice = message.text.lower()

    if user_choice not in spisok:
        await message.answer("Выбери: камень, ножницы или бумага")
        return

    bot_choice = random.choice(spisok)

    await message.answer(
        f"Ты выбрал: {user_choice}\n"
        f"Бот выбрал: {bot_choice}"
    )

    if user_choice == bot_choice:
        await message.answer("Ничья 🤝")
    elif (
        (user_choice == "камень" and bot_choice == "ножницы") or
        (user_choice == "ножницы" and bot_choice == "бумага") or
        (user_choice == "бумага" and bot_choice == "камень")
    ):
        await message.answer("Ты выиграл 🎉")
    else:
        await message.answer("Бот выиграл 🤖")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
