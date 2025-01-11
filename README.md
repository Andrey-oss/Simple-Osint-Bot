# ** Simple Osint Bot **

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)

## Description
**Simple OSINT Bot** is a straightforward and easy-to-use bot for performing basic [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) tasks. It provides functions for gathering information about:
- **BSSID** (MAC address of an access point)
- **IP address**

The project is designed to be simple yet extensible, making it suitable for a wide range of users

## Key Features
- **Modular Core**: This bot’s structure allows users to create their own modules that are automatically loaded when the bot starts. This approach makes the bot highly adaptable and easy to expand with new functionalities
- **Cross-Platform Compatibility**: Compatible with Linux, Windows, and macOS (tested on Arch Linux)
- **MIT License**: The project is open-source under the MIT license, making it free to use and modify

## Installation and Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/Andrey-oss/Simple-Osint-Bot
    cd Simple-Osint-Bot
    ```

2. Install required dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

3. Run the bot:
    ```bash
    python3 main.py
    ```

## Creating Your Own Module
To create your own module, simply add a Python file to the modules directory, and it will be loaded automatically when the bot starts. For more details, check [example module](modules/test_module.py)

## Requirements
- Python 3.8+ (tested on Python3.12)
- Compatibility: Linux, Windows, macOS (tested on Linux)

## Settings
You have to follow the instructions about setting up the bot, please read the [documentation](SETTINGS.md)

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details

## Feedback and Support
If you have any questions, suggestions, or need support, feel free to open an issue or contact us at:
- **Email**: [artemkartka@gmail.com](mailto:artemkartka@gmail.com)
- **Telegram**: [@feedbackchater](https://t.me/feedbackchater_bot)
