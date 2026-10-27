import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Selamat datang di warung kami.")


app = (
    ApplicationBuilder()
    .token(TOKEN)
    .connect_timeout(30)
    .read_timeout(30)
    .write_timeout(30)
    .pool_timeout(30)
    .get_updates_connect_timeout(30)
    .get_updates_read_timeout(30)
    .build()
)
app.add_handler(CommandHandler("start", start))

print("Bot jalan...")
app.run_polling()