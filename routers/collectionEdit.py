from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(F.text.lower() == "edit collections 💾")
async def cmd_edit_collections(message: Message):
    
    await message.answer(
            'Заглушка', 
            parse_mode=ParseMode.MARKDOWN_V2
        )