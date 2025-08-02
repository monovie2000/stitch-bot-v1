#main.py

import os
from telegram.ext import ApplicationBuilder
from telegram_bot import get_handlers

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    for handler in get_handlers():
        app.add_handler(handler)

    app.run_polling()