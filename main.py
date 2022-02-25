import json
import logging
import os

from decouple import config
from telegram import BotCommand
from telegram.ext import (CallbackQueryHandler, CommandHandler,
                          ConversationHandler, Filters, MessageHandler,
                          Updater)

import state
from command import borrow, general, notification, profile, register, search_book

PORT = int(os.environ.get('PORT', 5000))
TOKEN = config('BOT_TOKEN')
HOST = config('HOST')
URL_APP = config('URL_APP')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Set bot commands
    this_folder = os.path.dirname(os.path.abspath(__file__))
    listJson = os.path.join(this_folder, 'command/list.json')
    with open(listJson, "r") as read_file:
        cmd_list = json.load(read_file)

    commands = []
    for key, value in cmd_list.items():
        commands.append(BotCommand(key, value))

    updater.bot.setMyCommands(commands)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', general.start),
            CommandHandler('help', general.start),
            CommandHandler('registrasi', register.command),
            CommandHandler('caribuku', search_book.command),
            CommandHandler('profil', profile.command),
            CommandHandler('notifikasi', notification.command),
            CommandHandler('peminjaman', borrow.command),
        ],
        states={
            state.EMAIL: [
                MessageHandler(Filters.text & ~Filters.command, register.email)
            ],
            state.NAME: [
                MessageHandler(Filters.text & ~Filters.command, register.name)
            ],
            state.ADDRESS: [
                MessageHandler(Filters.text & ~Filters.command,
                               register.address)
            ],
            state.PHONE: [
                MessageHandler(Filters.text & ~Filters.command, register.phone)
            ],
            state.BOOK: [
                MessageHandler(Filters.text & ~Filters.command,
                               search_book.book)
            ],
            state.SHOWBOOK: [
                CallbackQueryHandler(search_book.show_book)
            ],
            state.NOTIFICATION: [
                CallbackQueryHandler(notification.button)
            ],
            state.SHOWBORROW: [
                CallbackQueryHandler(borrow.show_borrow)
            ]
        },
        fallbacks=[CommandHandler('cancel', general.cancel)],
    )

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    # updater.start_polling()
    updater.start_webhook(listen=HOST,
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url=URL_APP + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
