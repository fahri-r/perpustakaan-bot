import requests
from decouple import config
from state import SHOWBORROW
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, ConversationHandler

from command.general import clear_user_data, login


def command(update: Update, context: CallbackContext) -> int:
    context.user_data['telegram_id'] = update.message.from_user.id

    if not 'token' in context.user_data:
        login(context)

    url = f"{config('URL_API')}api/v1/members/{context.user_data['member_id']}/borrows"
    headers = {
        'Authorization': f"Bearer {context.user_data['token']}"
    }

    r = requests.get(url, headers=headers)

    if (r.status_code == 200):
        data = r.json()['data']
        keyboard = []
        for x in data:
            status = 'Selesai' if x['status'] else 'Aktif'
            keyboard.append([InlineKeyboardButton(
                f"{x['book']['title']} ({status})", callback_data=x['id'])])

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            'Daftar Buku Pinjaman:', reply_markup=reply_markup)

        return SHOWBORROW

    update.message.reply_text('Anda belum pernah meminjam buku.')
    clear_user_data(context)

    return ConversationHandler.END


def show_borrow(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    if not 'token' in context.user_data:
        login(context)

    url = f"{config('URL_API')}api/v1/borrows/{query.data}"
    headers = {
        'Authorization': f"Bearer {context.user_data['token']}"
    }

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()['data']
        message = (
            f"Detail Peminjaman\n"
            f"Judul Buku: {data['book']['title']}\n"
            f"Tanggal Pinjam: {data['borrow_date']}\n"
            f"Tanggal Kembali: {data['return_date']}\n"
            f"Status: {'Sudah Kembali' if data['status'] else 'Belum Kembali'}\n"
        )
    else:
        message = "Tidak dapat menampilkan detail Peminjaman."

    query.answer()

    query.edit_message_text(text=message)

    clear_user_data(context)
    return ConversationHandler.END
