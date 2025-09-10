from telebot import TeleBot
from telebot.types import Message

def admin_user(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Woy, admin!")
