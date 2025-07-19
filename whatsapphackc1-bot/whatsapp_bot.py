import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

BOT_TOKEN = "7995908825:AAG9DKcuPn2yGAVNoIMM9CsGKJq5Qu0f14Y"
ETH_ADDRESS = "0xb58937eB4D98E79e66522D32DDc6a4004ed74Ae9"
ETH_AMOUNT = 0.25
ETHERSCAN_API = "RT5SWH9PAWRJS8V79GRJZT3NCYR4233PKA"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to WhatsAppHackC1Bot!
Use /buy to see payment instructions.
Use /access after payment.
Use /help for support."
    )

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"💰 Send exactly {ETH_AMOUNT} ETH to:
{ETH_ADDRESS}

After payment, use /access to verify."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Commands:
/start - Welcome message
/buy - Payment info
/access - Verify payment
/status - Check bot status"
    )

async def access(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={ETH_ADDRESS}&sort=desc&apikey={ETHERSCAN_API}"
    try:
        response = requests.get(url).json()
        txs = response.get("result", [])
        for tx in txs:
            if (
                tx["from"].lower() == user.username.lower() or user.username.lower() in tx["input"].lower()
            ) and float(tx["value"]) / 1e18 >= ETH_AMOUNT:
                await update.message.reply_text("✅ Access Granted. You've paid.")
                return
        await update.message.reply_text("❌ No valid payment found. Make sure your transaction is confirmed.")
    except Exception as e:
        await update.message.reply_text("⚠️ Error verifying payment.")
        logger.error(f"Access check failed: {e}")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is up and running!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("access", access))
app.add_handler(CommandHandler("status", status))

app.run_polling()
