import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        types.KeyboardButton(text="Select collection 🥽"),
        types.KeyboardButton(text="Edit collections 💾"),
        types.KeyboardButton(text="New collection 🖍"),
        [
            types.KeyboardButton(text="Check health 🛠"),
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

@dp.message(F.text.lower() == "select collection 🥽")
async def cmd_start(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )

@dp.message(F.text.lower() == "edit collections 💾")
async def cmd_start(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )
    
@dp.message(F.text.lower() == "new collection 🖍")
async def cmd_start(message: types.Message):

    inline_buttons = [
        [
            types.InlineKeyboardButton(text="⏪ Back", callback_data="go back")
        ]
    ]
    
    inline_keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=inline_buttons
    )
    
    await message.answer(
            'Name for the new collection? Just type it', 
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=inline_keyboard
        )

@dp.message(F.text.lower() == "check health 🛠")
async def cmd_start(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )
    
@dp.message(F.text.lower() == "clear chat 🧹")
async def cmd_start(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )
    
if __name__ == '__main__':
    print("Starting bot...")
    dp.run_polling(bot)