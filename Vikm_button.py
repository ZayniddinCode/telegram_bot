from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, ConversationHandler, CallbackQueryHandler


stting_button=[
    [
    InlineKeyboardButton("Englsh 🇬🇧", callback_data="1"),
    InlineKeyboardButton("Ruscha 🇷🇺", callback_data="2"),
    ],
    [

    InlineKeyboardButton("O'zbekcha 🇺🇿",callback_data="3"),
    InlineKeyboardButton("Esp ",callback_data="4")
    ]

]


artist_button=[
    [
        InlineKeyboardButton("1", callback_data="1",url="https://youtu.be/6hAg2vyWwfI"),
        InlineKeyboardButton("2", callback_data="2",url="https://youtu.be/DDjeQdXVLow"),
        InlineKeyboardButton("3", callback_data="3",url="https://youtu.be/gnCR4EQqa20"),
        InlineKeyboardButton("4", callback_data="4"),
        InlineKeyboardButton("5", callback_data="5"),

    ],
    [
        InlineKeyboardButton("6", callback_data="6"),
        InlineKeyboardButton("7", callback_data="7"),
        InlineKeyboardButton("8", callback_data="8"),
        InlineKeyboardButton("9", callback_data="9"),
        InlineKeyboardButton("10", callback_data="10")

    ],
    [
        InlineKeyboardButton("➡", callback_data="11"),
        InlineKeyboardButton("❌", callback_data="12"),
        InlineKeyboardButton("⬅", callback_data="13"),

    ],

]
