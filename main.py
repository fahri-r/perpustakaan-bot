import json
import logging

from decouple import config
from telegram import BotCommand
from telegram.ext import (CallbackQueryHandler, CommandHandler,
                          ConversationHandler, Filters, MessageHandler,
                          Updater)

import state
from command import general, profile, register, search_book

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(config('BOT_TOKEN'))

    with open(".\command\list.json", "r") as read_file:
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
            ]
        },
        fallbacks=[CommandHandler('cancel', general.cancel)],
    )

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
