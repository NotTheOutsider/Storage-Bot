from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_back_button() -> list:    
    return [InlineKeyboardButton(text="⏪ Back", callback_data="go_back")]

def get_back_keyaboard() -> InlineKeyboardMarkup:
    ib = [
        get_back_button()
    ]
    
    return InlineKeyboardMarkup(
        inline_keyboard=ib
    )
    
def get_collection_list_keyaboard(collections: list[str]) -> InlineKeyboardMarkup:
    ib = []
    
    for collection in collections:
        ib.append([InlineKeyboardButton(text=collection, callback_data=collection)])
    
    ib.append(get_back_button())
    
    return InlineKeyboardMarkup(
        inline_keyboard=ib
    )