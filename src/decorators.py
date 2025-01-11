from src.printf import print_denied
from functools import wraps
from datetime import datetime

def id_checker(bot, user_id, log):
    def decorator(func):
        @wraps(func)
        def wrapper(message):
                if message.from_user.id in user_id:
                    return func(message)
                elif log == 1:
                    print_denied(f"Unauthorized user as ID: {message.chat.id}")
                bot.reply_to(message, "Unauthorized access")
        return wrapper
    return decorator