"""Configuration handler"""
import os
from pathlib import Path

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
APP_PATH = Path(CURRENT_DIR).parent

# log
LOG_PATH = str(APP_PATH) + os.environ.get("LOG_PATH", "/")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
LOG_FORMAT = os.environ.get("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
TIME_FORMAT = "%d-%m-%Y %H-%M"
BASE_URL = os.environ.get("BASE_URL")
SUBSCRIPTION_KEY = os.environ.get("SUBSCRIPTION_KEY")