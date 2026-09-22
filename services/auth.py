import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _config_path(environment_name, default_name):
  configured_path = os.getenv(environment_name)
  if configured_path:
    return Path(configured_path).expanduser()
  return PROJECT_ROOT / default_name


def get_drive_service():
  creds = None
  credentials_path = _config_path("GOOGLE_CREDENTIALS_PATH", "credentials.json")
  token_path = _config_path("GOOGLE_TOKEN_PATH", "token.json")

  if token_path.exists():
    creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      if not credentials_path.exists():
        raise FileNotFoundError(
            f"Google OAuth credentials not found at {credentials_path}. "
            "Download a desktop OAuth client JSON file and save it there, "
            "or set GOOGLE_CREDENTIALS_PATH."
        )
      flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
      creds = flow.run_local_server(host="localhost", port=3000)
    token_path.parent.mkdir(parents=True, exist_ok=True)
    with token_path.open("w", encoding="utf-8") as token:
      token.write(creds.to_json())

  try:
    return build("drive", "v3", credentials=creds)
  except HttpError as error:
    print(f"An error occurred: {error}")