from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

class MeliusTelegramBot:
    def __init__(self, token, engine):
        self.token = token
        self.engine = engine

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Melius Agent is online and ready to help via Telegram!")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_text = update.message.text
        response = self.engine.process_query(user_text)
        await update.message.reply_text(response)

    def run(self):
        if not self.token:
            print("Telegram Token not provided. Skipping Telegram bot.")
            return
        
        app = ApplicationBuilder().token(self.token).build()
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.handle_message))
        
        print("Telegram bot starting...")
        app.run_polling()
