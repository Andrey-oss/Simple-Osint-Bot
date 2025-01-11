from datetime import datetime

def print_error(text):
    print(f'[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [ERROR] {text}')

def print_warning(text):
    print(f'[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [WARN] {text}')

def print_debug(text):
    print(f'[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [DEBUG] {text}')

def print_denied(text):
    print(f'[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [DENIED] {text}')

def print_info(text):
    print(f'[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [INFO] {text}')

def print_fatal(text):
    exit(f'[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [FATAL] {text}')