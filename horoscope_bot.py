import logging
import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

zodiac_signs = [
    ['aries', 'taurus', 'gemini', 'cancer'],
    ['leo', 'virgo', 'libra', 'scorpio'],
    ['sagittarius', 'capricorn', 'aquarius', 'pisces']
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the Horoscope Bot! Please choose your zodiac sign:",
        reply_markup=ReplyKeyboardMarkup(zodiac_signs, one_time_keyboard=True)
    )


def get_horoscope(sign: str) -> str:
    try:
        # Use the deployed Flask API URL here
        url = f"https://horoscope-api-10.onrender.com/horoscope?sign={sign.lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('horoscope', 'Sorry, no horoscope found.')
        else:
            return "Sorry, couldn't fetch your horoscope."
    except Exception as e:
        logger.error(f"Error fetching horoscope: {e}")
        return "Sorry, couldn't fetch your horoscope."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    sign = update.message.text.lower()
    if sign in sum(zodiac_signs, []):
        horoscope = get_horoscope(sign)
        await update.message.reply_text(horoscope)
    else:
        await update.message.reply_text("Please choose a valid zodiac sign from the keyboard.")


def main() -> None:
    bot_token = "8358290464:AAFHr8oBUVEMGXoU7ICY5UzxrZ5dTl_3Sys"
    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == '__main__':
    main()
