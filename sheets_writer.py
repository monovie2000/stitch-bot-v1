# sheets_writer.py

import os, gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(os.getenv("GOOGLE_CREDENTIALS_PATH"), scope)
client = gspread.authorize(credentials)
sheet = client.open(os.getenv("GOOGLE_SHEET_NAME")).sheet1

def save_to_sheets(label, description, date, breakdown):
    sheet.append_row([label, description, date, breakdown])