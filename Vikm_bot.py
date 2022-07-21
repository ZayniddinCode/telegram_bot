from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    InlineQueryResultAudio, InputMediaAudio
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, ConversationHandler, \
    CallbackQueryHandler
from Vikm_button import *


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu aleykum\n\n/setlang\n/artist")

    return 1


def setlang(update: Update, context: CallbackContext):
    update.message.reply_text("Iltimos tilni tanlang",
                              reply_markup=InlineKeyboardMarkup(stting_button))

    return 2


def artist(update: Update, context: CallbackContext):
    update.message.reply_text("Qaysi qushiqni tanlaysiz")
    # reply_markup=InlineKeyboardMarkup(artist_button))

    return 3


def qushiq(update: Update, context: CallbackContext):
    qushiq = update.message.text
    query = update.callback_query
    user = update.message.from_user
    # chat_id=update.message.chat_id
    chat_id = f"{user.id}"
    if qushiq.lower() in "ramil":
        update.message.reply_text("1.Ramil siyay\n2.Ramil mayak\n2.Ramil levis",
                                  reply_markup=InlineKeyboardMarkup(artist_button))

    else:
        context.bot.sendAudio(chat_id=chat_id, audio=open("Ramil' - Маяк.mp3", 'rb'))
        print("as")


def main():
    TOKENT = "5387467512:AAEqwBomWDfxYI29TCbQzthTXsKU4LM4TeE"
    updater = Updater(TOKENT)

    all_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={

            1: [CommandHandler("setlang", setlang)],
            2: [CommandHandler("artist", artist)],
            3: [MessageHandler(Filters.text, qushiq)]
        },
        fallbacks=[]
    )
    updater.dispatcher.add_handler(all_handler)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
