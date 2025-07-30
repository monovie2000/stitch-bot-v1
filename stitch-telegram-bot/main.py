# main.py

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from secrets import TELEGRAM_BOT_TOKEN
from bot_logic import process_user_request

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👗 Hello! I’m Stitch, your fashion assistant.\n\nSend me a photo and short description of the outfit you'd like estimated.")

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    if not text:
        update.message.reply_text("Please send a description of the outfit.")
        return

    # Placeholder - add logic later to check image & text
    result = process_user_request("image_url_placeholder", text)

    # Format reply
    breakdown = result["breakdown"]
    reply = (
        f"📌 *Estimation Summary:*\n"
        f"🧵 Fabrics: {breakdown['fabrics']}\n"
        f"💸 Material Cost: {breakdown['material_cost']}\n"
        f"👷 Labor Cost: {breakdown['labor_cost']}\n"
        f"📈 Profit: {breakdown['profit_margin']}\n"
        f"💰 Total: {breakdown['total']}"
    )

    update.message.reply_text(reply, parse_mode='Markdown')

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()