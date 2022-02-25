import datetime

import pytz
import requests
from decouple import config
from state import NOTIFICATION
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, ConversationHandler

from command.general import clear_user_data, login


def command(update: Update, context: CallbackContext) -> None:
    context.user_data['telegram_id'] = update.message.from_user.id

    keyboard = [
        [
            InlineKeyboardButton(
                "Aktifkan", callback_data=update.message.from_user.id),
            InlineKeyboardButton("Matikan", callback_data='0'),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Notifikasi:', reply_markup=reply_markup)
    return NOTIFICATION


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if not 'token' in context.user_data:
        login(context)

    if query.data != '0':
        try:
            remove_job_if_exists(str(query.data), context)
            time = datetime.time(hour=8, minute=0, second=0,
                                 microsecond=0, tzinfo=pytz.timezone('Asia/Jakarta'))
            context.job_queue.run_daily(alarm, time, days=(
                0, 1, 2, 3, 4, 5, 6), context=context.user_data, name=str(query.data))

            # context.job_queue.run_repeating(alarm, 5, context=context.user_data, name=str(query.data))

            msg = 'Notifikasi berhasil diaktifkan.'
        except (IndexError, ValueError):
            msg = 'Notifikasi gagal diaktifkan.'
    else:
        context.job_queue.stop()
        msg = 'Notifikasi berhasil dimatikan.'

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=msg)
    clear_user_data(context)
    return ConversationHandler.END


def alarm(context: CallbackContext) -> None:
    job = context.job

    url = f"{config('URL_API')}api/v1/members/{job.context['member_id']}/borrows"
    headers = {
        'Authorization': f"Bearer {job.context['token']}"
    }
    params = {
        'return_date': datetime.datetime.now().date()
    }

    r = requests.get(url, params=params, headers=headers)

    if (r.status_code == 200):
        data = r.json()['data']
        for x in data:
            if not x['status']: 
                book = x['book']['title']
                context.bot.send_message(
                    job.name, text=f"Hari ini adalah jadwal pengembalian buku {book}.")


def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True
