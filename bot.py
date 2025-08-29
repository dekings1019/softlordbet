import logging
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Your bot token
BOT_TOKEN = "7136616747:AAHkEZGLqiYuvh8Uj6SXH5ONwu2A6VQ6Ggc"

# Start command
async def start(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm SoftlordBot 🤖")

# Main function to run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
