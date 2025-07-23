import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from routers import collectionSelect, collectionEdit, collectionCreate, checkHealth, clearChat
from keyboards import replyKeyboards

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()
dp.include_routers(
        collectionSelect.router, 
        collectionEdit.router,
        collectionCreate.router, 
        checkHealth.router,
        clearChat.router
    )

@dp.message(Command("start"))
async def cmd_start(message: types.Message):

    await message.answer(
        "Sup ma boy. Whaca want today?", 
        reply_markup=replyKeyboards.get_startup_keyaboard()
    )
    
if __name__ == '__main__':
    print("Starting bot...")
    dp.run_polling(bot)