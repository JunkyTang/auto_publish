import os

def validate_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError("Configuration file not found.")