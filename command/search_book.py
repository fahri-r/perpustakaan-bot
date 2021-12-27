import requests
from decouple import config
from state import BOOK, SHOWBOOK
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, ConversationHandler

from command.general import clear_user_data, login


def command(update: Update, context: CallbackContext) -> None:
    context.user_data['telegram_id'] = update.message.from_user.id

    update.message.reply_text(
        'Halo! Nama saya Perpustakaan Bot.'
        'Kirim /cancel untuk membatalkan proses pencarian buku.\n\n'
        'Apa judul buku yang anda cari?'
    )

    return BOOK


def book(update: Update, context: CallbackContext) -> int:
    context.user_data['title'] = update.message.text

    if not 'token' in context.user_data:
        login(context)

    url = f"{config('URL_API')}api/v1/books"
    params = {
        'title': context.user_data['title']
    }

    headers = {
        'Authorization': f"Bearer {context.user_data['token']}"
    }

    r = requests.get(url, params=params, headers=headers)

    if (r.status_code == 200):
        data = r.json()['data']
        keyboard = []
        for x in data:
            keyboard.append([InlineKeyboardButton(
                x['title'], callback_data=x['id'])])

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            'Hasil Pencarian:', reply_markup=reply_markup)

        return SHOWBOOK

    update.message.reply_text('Buku yang anda cari tidak dapat ditemukan.')
    clear_user_data(context)

    return ConversationHandler.END


def show_book(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    if not 'token' in context.user_data:
        login(context)

    url = f"{config('URL_API')}api/v1/books/{query.data}"
    headers = {
        'Authorization': f"Bearer {context.user_data['token']}"
    }

    r = requests.get(url, headers=headers)
    data = r.json()['data']
    message = (
        f"Judul: {data['title']}\n"
        f"Deskripsi: {data['description']}\n"
        f"Tahun Terbit: {data['year']}\n"
        f"Pengarang: {data['author']}\n"
        f"Jumlah Buku Tersedia: {data['qty']}\n"
    )

    query.answer()

    query.edit_message_text(text=f"Detail Buku\n{message}")

    clear_user_data(context)
    return ConversationHandler.END
