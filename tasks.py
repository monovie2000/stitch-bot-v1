# tasks.py

import datetime
from imgbb import upload_image_to_imgbb
from deepseek_api import analyze_fashion
from sheets_writer import save_to_sheets
from utils import sanitize_input

async def process_user_request(update, context):
    user_input = sanitize_input(update.message.caption or update.message.text or "")

    if not user_input:
        await update.message.reply_text("❗️Please include a short description of the outfit.")
        return

    if not update.message.photo:
        await update.message.reply_text("📸 Please upload a photo of the outfit along with the description.")
        return

    await update.message.reply_text("🧵 Processing your request...")

    # Download image
    photo = await update.message.photo[-1].get_file()
    image_bytes = await photo.download_as_bytearray()

    # Upload to imgbb
    image_url = upload_image_to_imgbb(image_bytes)

    # Analyze with AI
    result = analyze_fashion(user_input, image_url)

    # Save to Sheets
    save_to_sheets(
        label=user_input[:30],
        description=user_input,
        date=str(datetime.date.today()),
        breakdown=result
    )

    # Reply to user
    await update.message.reply_text(f"✅ Estimate ready:\n{result}")