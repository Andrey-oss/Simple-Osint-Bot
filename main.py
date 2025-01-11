from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from core.mod_manager import ModuleLoader
from src.settings import config
from src.decorators import id_checker
import telebot

__VERSION__ = "0.0.1-beta"

user_id = config()['id']  # UserID
api = config()['api_key']  # API key
pm = config()['parse_mode'] # Parse mode
debug_level = config()['enable_debugging'] # Debug

bot = telebot.TeleBot(api, parse_mode=pm)

loader = ModuleLoader(debug=debug_level)
loader.load_modules()

@bot.message_handler(commands=['start'])
@id_checker(bot, user_id, debug_level)
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome @{message.from_user.username}!")
    show_module_functions(message)

def show_module_functions(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for module in loader.list_loaded_modules():
        fcn = loader.name_by_fcn(module)
        for func_name, display_name in fcn.items():
            keyboard.add(KeyboardButton(display_name))
    bot.send_message(message.chat.id, "Choose option:", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
@id_checker(bot, user_id, debug_level)
def get_msg(message):
    if message.text == "Back":
        send_welcome(message)
    else:
        markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn = KeyboardButton(text='Back')
        markup.add(btn)
        kb_mark = loader.kb_markup(message.text)
        inp = bot.reply_to(message, kb_mark[2], reply_markup=markup)
        def run_fcn_with_args(user_input):
            if user_input.text not in ['/start', "Back"]:
                result = loader.call_module_function(kb_mark[0], kb_mark[1], user_input.text)
                bot.send_message(user_input.chat.id, f"\n{result}")
                send_welcome(message)
            else:
                send_welcome(message)
        bot.register_next_step_handler(inp, run_fcn_with_args)

bot.infinity_polling()
