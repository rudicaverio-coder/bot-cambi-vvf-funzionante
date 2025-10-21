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
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_keyboard():
    keyboard = [
        [KeyboardButton("📅 Chi Tocca"), KeyboardButton("👥 VVF")],
        [KeyboardButton("🔄 Cambi"), KeyboardButton("❓ Help")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != MY_USER_ID:
        await update.message.reply_text("❌ Accesso riservato")
        return
        
    await update.message.reply_text(
        "🤖 **Bot Gestione Cambi VVF**\n\nSeleziona un'opzione:",
        reply_markup=get_keyboard()
    )

async def handle_message(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != MY_USER_ID:
        await update.message.reply_text("❌ Accesso riservato")
        return
        
    text = update.message.text
    
    if text == "📅 Chi Tocca":
        await update.message.reply_text("📅 **CHI TOCCA OGGI**\n\n• Sera: S4\n• Notte: Bn")
    elif text == "👥 VVF":
        await update.message.reply_text("👥 **GESTIONE VVF**\n\nFunzione in sviluppo")
    elif text == "🔄 Cambi":
        await update.message.reply_text("🔄 **GESTIONE CAMBI**\n\nFunzione in sviluppo")
    elif text == "❓ Help":
        await update.message.reply_text("❓ **HELP**\n\nUsa i pulsanti per navigare")
    else:
        await update.message.reply_text("Usa i pulsanti qui sotto:", reply_markup=get_keyboard())

def main():
    logger.info("🚀 Avvio Bot Cambi VVF...")
    
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN_CAMBI non configurato")
        return
    
    # Crea applicazione
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Aggiungi handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logger.info("✅ Bot avviato con successo!")
    logger.info("📍 Modalità: Polling")
    
    # Avvia il bot
    application.run_polling()

if __name__ == '__main__':
    main()
