from enum import Enum

from google.oauth2 import service_account

GOOGLE_CREDENTIALS = service_account.Credentials.from_service_account_file(
    "../credentials.json",
    scopes=["https://www.googleapis.com/auth/spreadsheets"],
)


class SheetTypes(Enum):
    CONGRESO_AVANCES = "AVANCES-RAW"
    CONGRESO_RESULTADOS = "RES-C-MUN-RAW"
    SENADO_RESULTADOS = "RES-S-MUN-RAW"
