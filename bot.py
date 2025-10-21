# bot.py - VERSIONE ULTRA-SEMPLICE GARANTITA
#GitHub per Gist:  g h p _ q n F F B t U P Y q 0 8 a c r 3 S j j W H w n 5 J i g P C A 2 5 1 i F c
#Github Gist backup:98e323b6ad67035edf13a6d57f97ffe1
import os
import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Configurazione
BOT_TOKEN = os.environ.get('BOT_TOKEN_CAMBI')
MY_USER_ID = 1816045269

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Tastiera
def get_keyboard():
    return ReplyKeyboardMarkup([
        [KeyboardButton("📅 Chi Tocca"), KeyboardButton("👥 VVF")],
        [KeyboardButton("🔄 Cambi"), KeyboardButton("❓ Help")]
    ], resize_keyboard=True)

# Comando start
async def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != MY_USER_ID:
        await update.message.reply_text("❌ Accesso negato")
        return
        
    await update.message.reply_text(
        "🤖 **Bot Cambi VVF**\n\nUsa i pulsanti qui sotto:",
        reply_markup=get_keyboard()
    )

# Gestione messaggi
async def handle_message(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != MY_USER_ID:
        await update.message.reply_text("❌ Accesso negato")
        return
        
    text = update.message.text
    
    if text == "📅 Chi Tocca":
        await update.message.reply_text("🔧 Funzione in sviluppo")
    elif text == "👥 VVF":
        await update.message.reply_text("🔧 Gestione VVF in sviluppo")
    elif text == "🔄 Cambi":
        await update.message.reply_text("🔧 Gestione cambi in sviluppo")
    elif text == "❓ Help":
        await update.message.reply_text("ℹ️ Bot in fase di setup")
    else:
        await update.message.reply_text("Usa i pulsanti", reply_markup=get_keyboard())

# Main
def main():
    logger.info("🚀 Avvio bot...")
    
    # Crea app
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("🤖 Bot avviato - Polling mode")
    app.run_polling()

if __name__ == '__main__':
    main()
