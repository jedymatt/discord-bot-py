import imp
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN') or ''
API_TOKEN = os.getenv('API_TOKEN') or ''
API_BASE_URL = os.getenv('API_BASE_URL') or ''
