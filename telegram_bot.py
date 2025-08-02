# telegram_bot.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from tasks import process_user_request
from logger import log_error

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I’m Stitch, your fashion estimation assistant. Send me a picture and style description to get started.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use this format:\n1. Upload image of outfit\n2. Add style description\nStitch will analyze and estimate fabric, labor, and cost.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await process_user_request(update, context)
    except Exception as e:
        log_error(e)
        await update.message.reply_text("❗️Something went wrong. Please try again or type /help")

def get_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("help", help_command),
        MessageHandler(filters.TEXT | filters.PHOTO, handle_message)
    ]