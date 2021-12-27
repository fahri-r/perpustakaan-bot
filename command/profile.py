import requests
from decouple import config
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from command.general import clear_user_data, login


def command(update: Update, context: CallbackContext) -> int:
    context.user_data['telegram_id'] = update.message.from_user.id
    
    if not 'token' in context.user_data:
        login(context)

    member_id = context.user_data['member_id']
    url = f"{config('URL_API')}api/v1/members/{member_id}"
    headers = {
        'Authorization': f"Bearer {context.user_data['token']}"
    }

    r = requests.get(url, headers=headers)

    if (r.status_code == 200):
        data = r.json()['data']
        message = (
            f"Profil Member\n"
            f"Nama Lengkap: {data['name']}\n"
            f"Alamat: {data['address']}\n"
            f"No. HP: {data['phone']}\n"
            f"Email: {data['user']['email']}\n"
        )
    else:
        message = 'Data member tidak ditemukan.'

    update.message.reply_text(message)

    clear_user_data(context)

    return ConversationHandler.END
