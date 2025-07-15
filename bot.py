import os
import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Select collection 🥽")],
        [types.KeyboardButton(text="Edit collections 💾")],
        [
            types.KeyboardButton(text="Chech health 🛠"),
            types.KeyboardButton(text="Clear chat 🧹")
        ] 
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Push buttons, don't be distracted by the text"
    )
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Sup ma boy. Whaca want today?", reply_markup=keyboard)

@dp.message(F.text.lower() == "отвязать телеграм от всех конфигураций")
async def cmd_start(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )

@dp.message(F.text.lower() == "отвязать телеграм от всех конфигураций")
async def cmd_start(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )

@dp.message(F.text.lower() == "отвязать телеграм от всех конфигураций")
async def cmd_start(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )
    
@dp.message(F.text.lower() == "отвязать телеграм от всех конфигураций")
async def cmd_start(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )
    
if __name__ == '__main__':
    dp.run_polling(bot)