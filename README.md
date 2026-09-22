# Goodnotes RAG

## Requirements

- Windows
- Python 3.12 or newer
- A Google Cloud project with the Google Drive API enabled

## Setup from a fresh clone

Open PowerShell in the repository directory and run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Python 3.12 is the recommended baseline. If several Python versions are installed, run the command with the desired interpreter explicitly.

The repository virtual environment is intentionally not committed. Recreate it on each computer instead of copying `venv` or `.venv` between machines.

## Google Drive authentication

1. In Google Cloud Console, enable the Google Drive API.
2. Create an OAuth client ID with application type **Desktop app**.
3. Download the client JSON file and save it as `credentials.json` in the repository root.
4. Start the application. A browser window opens for authorization on the first run.
5. The generated `token.json` is local to that computer and is ignored by Git.

To store these files elsewhere, set optional PowerShell environment variables before starting:

```powershell
$env:GOOGLE_CREDENTIALS_PATH = "C:\path\to\credentials.json"
$env:GOOGLE_TOKEN_PATH = "C:\path\to\token.json"
```

The Drive folder ID defaults to the current Goodnotes folder. Override it with:

```powershell
$env:GOODNOTES_FOLDER_ID = "your-folder-id"
```

## Run

```powershell
.\.venv\Scripts\python.exe main.py
```

The ingestion package can also be run directly:

```powershell
.\.venv\Scripts\python.exe -m services.ingestion
```

Do not run `services\ingestion\__main__.py` as a standalone file; package-relative imports require the module command above.