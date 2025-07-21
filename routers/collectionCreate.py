from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()

class Form(StatesGroup):
    waiting_for_folder_name = State()

@router.message(F.text.lower() == "new collection 🖍", StateFilter(None))
async def cmd_create_collection(message: Message, state: FSMContext):

    inline_buttons = [
        [InlineKeyboardButton(text="⏪ Back", callback_data="go_back")]
    ]
    
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=inline_buttons
    )
    
    sent_message = await message.answer(
            'Name for the new collection? Just type it', 
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=inline_keyboard
        )
    
    await state.set_state(Form.waiting_for_folder_name)
    
@router.callback_query(F.data == "go_back")
async def retun_to_main(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()

    await callback.message.answer(
        'As you say man, going back\\. Am just working here 🤠',
        parse_mode=ParseMode.MARKDOWN_V2
    )

    await state.clear()

@router.message(F.text, Form.waiting_for_folder_name)
async def collection_name_chosen(message: Message, state: FSMContext):
    collection_name = message.text.strip()
    if not collection_name:
        sent_message = await message.answer(
            'Do not act stupid\\. Are you for real trying to put *blank spaces* as the name of the collection? 🤨',
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return
    if len(collection_name) > 25:
        sent_message = await message.answer(
            'Boooring 😴💤 Can you make it *shorter* man?',
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return

    await message.answer(
        f'New collection `{message.text}` has been created',
        parse_mode=ParseMode.MARKDOWN_V2
    )

    await state.clear()
