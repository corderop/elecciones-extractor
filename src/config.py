import os

from dotenv import load_dotenv

load_dotenv(".env")

ELECCIONES_USER = os.getenv("ELECCIONES_USER")
ELECCIONES_PASSWORD = os.getenv("ELECCIONES_PASSWORD")

GSHEET_ID = os.getenv("GSHEET_ID")
