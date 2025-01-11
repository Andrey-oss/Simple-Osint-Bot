from src.printf import print_fatal
import json

def config():
    try:
        with open("configs/settings.json", "r+") as cfg:
            cfg = json.load(cfg)
    except Exception:
        print_fatal("Cannot open settings.json file!")
    else:
        return cfg