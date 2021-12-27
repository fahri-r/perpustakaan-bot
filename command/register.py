import requests
from decouple import config
from state import ADDRESS, EMAIL, NAME, PHONE
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from command.general import clear_user_data


def command(update: Update, context: CallbackContext) -> None:
    context.user_data['telegram_id'] = update.message.from_user.id

    update.message.reply_text(
        'Halo! Nama saya Perpustakaan Bot. '
        'Kirim /cancel untuk membatalkan proses registrasi.\n\n'
        'Silakan masukan email anda.'
    )

    return EMAIL


def email(update: Update, context: CallbackContext) -> int:
    context.user_data['email'] = update.message.text

    update.message.reply_text(
        'Silakan masukan nama lengkap anda.'
    )

    return NAME


def name(update: Update, context: CallbackContext) -> int:
    context.user_data['name'] = update.message.text

    update.message.reply_text(
        'Silakan masukan alamat lengkap anda.'
    )

    return ADDRESS


def address(update: Update, context: CallbackContext) -> int:
    context.user_data['address'] = update.message.text

    update.message.reply_text(
        'Silakan masukan nomor telepon anda.'
    )

    return PHONE


def phone(update: Update, context: CallbackContext) -> int:
    context.user_data['phone'] = update.message.text

    url = f"{config('URL_API')}api/v1/members"
    data = {
        'email': context.user_data['email'],
        'name': context.user_data['name'],
        'address': context.user_data['address'],
        'phone': context.user_data['phone'],
        'telegram_id': context.user_data['telegram_id']
    }

    r = requests.post(url, data)

    if (r.status_code == 201):
        message = 'Registrasi berhasil dilakukan. Silakan lakukan verifikasi email terlebih dahulu.'
    elif (r.status_code == 422):
        message = 'Registrasi gagal. Pastikan pertanyaan diatas diisi dengan benar.'
    else:
        message = 'Registrasi gagal.'

    update.message.reply_text(message)

    clear_user_data(context)

    return ConversationHandler.END
