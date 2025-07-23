from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_startup_keyaboard() -> ReplyKeyboardMarkup:
    kb = [
            [KeyboardButton(text="Select collection 🥽")],
            [KeyboardButton(text="Edit collections 💾")],
            [KeyboardButton(text="New collection 🖍")],
            [
                KeyboardButton(text="Check health 🛠"),
                KeyboardButton(text="Clear chat 🧹")
            ]
        ]

    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Push buttons, don't be distracted by the text"
    )