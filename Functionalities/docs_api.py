# CREDENTIALS_FILE = 'credentials.json'
# DOC_TITLE = "My New Document"

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
redirect_uri = "http://localhost:8000/oauth/callback"

def create_blank_document(CREDENTIALS_FILE, DOC_TITLE):
    SCOPES = ['https://www.googleapis.com/auth/documents']
    # Initialize credentials flow
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    # Get user credentials
    credentials = flow.run_local_server(port=0)
    # Build the Docs service object
    service = build('docs', 'v1', credentials=credentials)
    # Create a new document body
    body = {
        'title': DOC_TITLE
    }
    # Create the document
    document = service.documents().create(body=body).execute()
    print(f"Doc created with ID: {document.get('id')}")
