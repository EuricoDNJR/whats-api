import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    ENV: str = os.getenv("ENV")
    WHATSAPP_TOKEN: str = os.getenv("WHATSAPP_TOKEN")
    PHONE_NUMBER_ID: str = os.getenv("PHONE_NUMBER_ID")
    VERIFY_TOKEN: str = os.getenv("VERIFY_TOKEN")


settings = Settings()
