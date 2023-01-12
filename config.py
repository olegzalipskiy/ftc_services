import os
from dotenv import load_dotenv

from src.utils.file_system import FileSystem

dotenv_path = FileSystem.get_absolute_path('.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

BASE_URL = os.environ.get("BASE_URL")
USER_PHONE = os.environ.get("USER_PHONE")
