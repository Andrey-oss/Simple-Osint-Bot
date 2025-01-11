# SETTINGS.md

This file describes the configuration settings for **Simple OSINT Bot**. The settings are specified in JSON format and control key aspects of the bot's functionality, such as API keys, message parsing modes, and debugging

## Bot Settings

- **id**:
  A list of user IDs that the bot can interact with. This is typically left empty or configured to include the specific users permitted to use the bot

- **api_key**:
  Your API key to access the bot's platform. This key is required for authorization, so ensure it is kept secure

- **parse_mode**:
  Sets the format for parsing messages. By default, this is set to `"HTML"` so that messages can include HTML styling

## Debugging/Logging Settings

- **enable_debugging**:
  Controls whether debugging information is printed to logs. Set to `1` to enable debugging or `0` to disable it
