import telebot

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I am your Telegram bot.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Bot is polling...")
    bot.polling()