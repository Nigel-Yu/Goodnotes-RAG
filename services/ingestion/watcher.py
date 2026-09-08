import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# from .constants import FOLDER_ID
from services.auth import get_drive_service

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]

def get_start_page_token(service):
  try:
    response = service.changes().getStartPageToken().execute()
    print(f"Start Token: {response}")
    return response.get("startPageToken")
  except HttpError as error:
    print(f"An error occurred: {error}")

def fetch_changes(service=get_drive_service()):
  try:
    page_token = get_start_page_token(service)

    while page_token is not None:
      response = service.changes().list(pageToken=page_token, spaces="drive").execute()
      print(response)
      # for change in response.get("changes"):
        # print(f"New change in {change.get("fileId")}")
      
  except HttpError as error:
    print(f"An error occured: {error}")

if __name__ == "__main__":
  fetch_changes()