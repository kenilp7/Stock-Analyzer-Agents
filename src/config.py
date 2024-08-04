import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

HF_TOKEN = os.getenv("HF_TOKEN", "ENTER_YOUR_HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME", "ENTER_MODEL_NAME")  # Example model name