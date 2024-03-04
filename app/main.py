import telebot
from config import TOKEN_TELEGRAM, TOKEN_OPENAI
from openai import OpenAI

client = OpenAI(api_key=TOKEN_OPENAI)

bot = telebot.TeleBot(TOKEN_TELEGRAM, parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def answer_all(message):
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a programming assistant, helping users with Python programming."},
            {"role": "user","content": message.text,}
        ],
        model="gpt-3.5-turbo",
    )
    result = completion.choices[0].message.content
    bot.reply_to(message, result)

if __name__ == "__main__":
    bot.polling()