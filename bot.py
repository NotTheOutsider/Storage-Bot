import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

class Form(StatesGroup):
    waiting_for_folder_name = State()

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

@dp.message(F.text.lower() == "select collection 🥽")
async def cmd_select_collection(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )

@dp.message(F.text.lower() == "edit collections 💾")
async def cmd_edit_collections(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )
    
@dp.message(F.text.lower() == "new collection 🖍", StateFilter(None))
async def cmd_create_collection(message: types.Message, state: FSMContext):

    inline_buttons = [
        [
            types.InlineKeyboardButton(text="⏪ Back", callback_data="go_back")
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
    
    await state.set_state(Form.waiting_for_folder_name)
    
@dp.callback_query(F.data == "go_back")
async def retun_to_main(callback: types.CallbackQuery):
    await callback.message.answer(
        'I love being silly'
    )

@dp.message(Form.waiting_for_folder_name, F.text)
async def food_chosen(message: types.Message, state: FSMContext):
    await message.answer(
        f'New collection {message.text} has been created',
    )
    await state.clear()

@dp.message(F.text.lower() == "check health 🛠")
async def cmd_check_health(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )
    
@dp.message(F.text.lower() == "clear chat 🧹")
async def cmd_clear_chat(message: types.Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )
    
if __name__ == '__main__':
    print("Starting bot...")
    dp.run_polling(bot)