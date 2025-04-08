from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import os
import io

# Define the scopes for access
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Authenticate and create the Drive API client
flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json', SCOPES)  # Path to your credentials file
creds = flow.run_local_server(port=0)

service = build('drive', 'v3', credentials=creds)

# ID of the file you want to download
file_id = '1BUrBhGO17382z5Kp-WzOnQDruK2LCXQn'  # Replace with your actual file ID

# Get the file metadata
request = service.files().get_media(fileId=file_id)
fh = io.FileIO('downloaded_file.pdf', 'wb')  # The file will be saved as 'downloaded_file.pdf'
downloader = MediaIoBaseDownload(fh, request)

done = False
while done is False:
    status, done = downloader.next_chunk()
    print(f"Download {int(status.progress() * 100)}%.")
