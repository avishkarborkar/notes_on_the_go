import streamlit as st
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from Functionalities.camera_input import get_camera_input
from Functionalities.upload_input import get_uploaded_input
from Functionalities.text_extraction import get_text_from_image
from Functionalities.docs_api import create_blank_document


# Define your SCOPES and redirect URI
SCOPES = ['https://www.googleapis.com/auth/documents']
redirect_uri = "http://localhost:8000/oauth/callback"

def create_google_docs_service():
    """Create Google Docs service."""
    creds = None
    # Initialize OAuth flow
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    # Build the Docs service object
    service = build('docs', 'v1', credentials=creds)
    return service


def create_blank_document(service, doc_title):
    """Create a blank Google Docs document."""
    body = {'title': doc_title}
    document = service.documents().create(body=body).execute()
    return document.get('documentId')

# Streamlit app starts here
st.title('Make notes on the go...')
use_camera = st.checkbox("Use Camera")
if use_camera:
    image_file = get_camera_input()
else:
    image_file = get_uploaded_input()

col1, col2 = st.columns(2)
show_image = col1.checkbox("Show Image")
show_text = col2.checkbox("Show Text")

image_container = st.container()
if show_image:
    with image_container:
        if image_file is not None:
            st.image(image_file)
        else:
            st.write("No image available")

if show_text:
    img_to_text = get_text_from_image(image_file)
    if img_to_text is not None:
        extracted_text = st.text_area("Extracted Text:", img_to_text, height=200)
        # User options for writing to documents
        write_to_options = st.selectbox("Write To:", ("New Document", "Existing Document"))
        if write_to_options == "New Document":
            doc_title = st.text_input("New Document Title:")
            if st.button("Create and Write"):
                # Create Google Docs service
                service = create_google_docs_service()
                if service:
                    doc_id = create_blank_document(service, doc_title)
                    st.success(f"New document created with ID: {doc_id}")
        else:
            st.write("Existing Document functionality not implemented yet.")
    else:
        st.write("No image selected or text extraction failed.")
