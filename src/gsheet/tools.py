import csv

from googleapiclient.discovery import build

from config import GSHEET_ID
from gsheet.types import GOOGLE_CREDENTIALS, SheetTypes


def send_information_to_gsheet(sheet_name: SheetTypes, data: str):
    print("Sending information to:", sheet_name.value)

    reader = csv.reader(data.splitlines(), delimiter=";")
    data = list(reader)

    service = build("sheets", "v4", credentials=GOOGLE_CREDENTIALS)
    service.spreadsheets().values().clear(
        spreadsheetId=GSHEET_ID,
        range=sheet_name.value,
    ).execute()
    service.spreadsheets().values().update(
        spreadsheetId=GSHEET_ID,
        range=sheet_name.value,
        valueInputOption="USER_ENTERED",
        body={"values": data},
    ).execute()
