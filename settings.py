import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('API_URL') or ''
TEST_EMAIL = os.getenv('TEST_EMAIL') or ''
TEST_PASSWORD = os.getenv('TEST_PASSWORD') or ''
TEST_NAME = os.getenv('TEST_NAME') or ''