from aiogram import Router, F
from aiogram.types import Message,  CallbackQuery
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards import inlineKeyboards

router = Router()

@router.message(F.text.lower() == "select collection 🥽")
async def cmd_select_collection(message: Message):
    
    await message.answer(
            'All yours collections are here:', 
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=inlineKeyboards.get_collection_list_keyaboard()
        )