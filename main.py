import json
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("bot_token"), parse_mode="HTML")
users_path = "users.json"
users = []


def load_users():
    global users
    users = json.load(open(users_path, "r"))

@bot.message_handler(commands=['all', "everyone", "все", "ау"])
def all_handler(message: telebot.types.Message):
    msg = "<b>⭐Ау животные вас отметили:</b>"
    for i in users:
        if i[0] != "@":
            msg += f"@{i} "
        else:
            msg += f"{i} "
    bot.reply_to(message, msg)


if __name__ == '__main__':
    load_users()
    bot.infinity_polling()