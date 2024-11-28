import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import Router
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the bot token from environment variables
API_TOKEN = os.getenv("API_TOKEN")

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
router = Router()

# Echo handler
@router.message()
async def echo(message: types.Message):
    await message.answer(message.text)

# Main entry point to run the bot
async def main():
    dp = Dispatcher()

    # Register the router to the dispatcher
    dp.include_router(router)

    # Start polling (await the coroutine)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    # Run the bot within an event loop
    asyncio.run(main())
