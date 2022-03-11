import json
import os

import requests
from decouple import config
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler


def start(update: Update, context: CallbackContext) -> None:
    this_folder = os.path.dirname(os.path.abspath(__file__))
    listJson = os.path.join(this_folder, 'list.json')
    with open(listJson, "r") as read_file:
        cmd_list = json.load(read_file)

    message_cmd = ""
    for key, value in cmd_list.items():
        cmd = f"/{key} - {value}\n"
        message_cmd = f"{message_cmd}{cmd}"

    message = (
        "Hai nama saya Perpustakaan Bot. Saya dapat membantu anda untuk mendapatkan informasi mengenai data-data pada perpustakaan.\n"
        "Anda dapat mengontrol saya dengan mengirimkan perintah berikut:\n"
        f"{message_cmd}"
    )
    update.message.reply_text(message)


def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Terimakasih sudah menggunakan Perpustakaan Bot ^_^'
    )

    clear_user_data(context)

    return ConversationHandler.END


def clear_user_data(context: CallbackContext) -> int:
    user_data = context.user_data
    if 'token' and 'member_id' in user_data:
        token = user_data['token']
        member_id = user_data['member_id']
        user_data.clear()
        user_data['token'] = token
        user_data['member_id'] = member_id
    else:
        user_data.clear()


def login(context: CallbackContext) -> int:
    user_data = context.user_data
    url = f"{config('URL_API')}api/v1/login/telegram"
    data = {
        'telegram_id': user_data['telegram_id']
    }
    r = requests.post(url, data)
    if (r.status_code == 200):
        user_data['token'] = r.json()['data']['token']
        user_data['member_id'] = r.json()['data']['member_id']
    else:
        start
