import telebot
from config import TOKEN_TELEGRAM, TOKEN_OPENAI
from openai import OpenAI
from datalog import db_user

client = OpenAI(api_key=TOKEN_OPENAI)

bot = telebot.TeleBot(TOKEN_TELEGRAM, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
#    db_user.add_user(message.from_user.username, message.from_user.user.id)
    bot.reply_to(message, "Привет, я бот, если хочешь узнать обо мне, спроси меня об этом.")

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