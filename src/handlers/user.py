import time
from telebot import TeleBot
from telebot.types import Message

def any_user(message: Message, bot: TeleBot):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    mention = f"[{first_name}](tg://user?id={user_id})"

    bot.send_message(message.chat.id, f"Halo, {mention}!", parse_mode="Markdown")

def ping(message: Message, bot: TeleBot):
    start = time.time()
    sent = bot.send_message(message.chat.id, "Checking⏱...")
    end = time.time()
    latency = (end - start) * 1000
    bot.edit_message_text(f"Pong🏓! {latency:.2f} ms", message.chat.id, sent.message_id)
