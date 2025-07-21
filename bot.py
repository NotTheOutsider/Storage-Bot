import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from routers import collectionSelect, collectionEdit, collectionCreate, checkHealth, clearChat

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
    kb = [
        [types.KeyboardButton(text="Select collection 🥽")],
        [types.KeyboardButton(text="Edit collections 💾")],
        [types.KeyboardButton(text="New collection 🖍")],
        [
            [types.KeyboardButton(text="Check health 🛠")],
            [types.KeyboardButton(text="Clear chat 🧹")]
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Push buttons, don't be distracted by the text"
    )

    await message.answer("Sup ma boy. Whaca want today?", reply_markup=keyboard)
    
if __name__ == '__main__':
    print("Starting bot...")
    dp.run_polling(bot)