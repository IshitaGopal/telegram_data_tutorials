import os
from dotenv import load_dotenv

# load enviroment variables from the .env file
load_dotenv()


class Config:
    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    phone = os.getenv("PHONE_NUM")
    session_name = "anon.session"
    output_dir = "json_data"
