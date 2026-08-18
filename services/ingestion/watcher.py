import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
FOLDER_ID = "1AYkSBoEjWW7jq6OW94aB72Om9zYL_zFV" # Goodnotes folder

# def download_file(service, file_id, file_name):
  # request = service.files().get(file_id, acknowledgeAbuse=True, supportsAllDrives=False, )

def main():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  # stores access & refresh tokens, created auomatically when authorization completed for the first time

  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(host="localhost", port=3000)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("drive", "v3", credentials=creds)

    # Call the Drive v3 API
    # results = (
    #     service.files()
    #     .list(pageSize=50, fields="nextPageToken, files(id, name)")
    #     .execute()
    # )
    results = (
      service.files()
      .list(q=f"'{FOLDER_ID}' in parents")
      .execute()
    )
    items = results.get("files", [])
    # items = results.get(FOLDER_ID)

    if not items:
      print("No files found.")
      return
    print("Files:")
    for item in items:
      print(f"{item['name']} ({item['id']})")
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")