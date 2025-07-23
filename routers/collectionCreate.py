from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards import inlineKeyboards

router = Router()

class Form(StatesGroup):
    waiting_for_folder_name = State()

@router.message(F.text.lower() == "new collection 🖍", StateFilter(None))
async def cmd_create_collection(message: Message, state: FSMContext):
    
    sent_message = await message.answer(
            'Name for the new collection? Just type it', 
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=inlineKeyboards.get_back_keyaboard()
        )
    
    await state.update_data(message_ids_to_delete=[sent_message.message_id, message.message_id])
    await state.set_state(Form.waiting_for_folder_name)
    
@router.callback_query(F.data == "go_back")
async def retun_to_main(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    message_ids_to_delete = data.get("message_ids_to_delete", [])
    await callback.bot.delete_messages(chat_id=callback.message.chat.id, message_ids=message_ids_to_delete)

    await callback.message.answer(
        'As you say man, going back\\. Am just working here 🤠',
        parse_mode=ParseMode.MARKDOWN_V2
    )

    await state.clear()

@router.message(F.text, Form.waiting_for_folder_name)
async def collection_name_chosen(message: Message, state: FSMContext):
    data = await state.get_data()
    message_ids_to_delete = data.get("message_ids_to_delete", [])
    message_ids_to_delete.append(message.message_id)

    collection_name = message.text.strip()

    if not collection_name:
        error_message = await message.answer(
            'Do not act stupid\\. Are you for real trying to put *blank spaces* as the name of the collection? 🤨',
            parse_mode=ParseMode.MARKDOWN_V2
        )

        message_ids_to_delete.append(error_message.message_id)
        await state.update_data(message_ids=message_ids_to_delete)
        return
    if len(collection_name) > 25:
        error_message = await message.answer(
            'Boooring 😴💤 Can you make it *shorter* man?',
            parse_mode=ParseMode.MARKDOWN_V2
        )

        message_ids_to_delete.append(error_message.message_id)
        await state.update_data(message_ids=message_ids_to_delete)
        return
    
    await message.bot.delete_messages(chat_id=message.chat.id, message_ids=message_ids_to_delete)

    await message.answer(
        f'New collection `{message.text}` has been created',
        parse_mode=ParseMode.MARKDOWN_V2
    )

    await state.clear()
