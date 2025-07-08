
import os

ALLOWED_EXTENSIONS = {'.pdf', '.jpg', '.jpeg', '.png', '.txt'}
ALLOWED_MIME_TYPES = {
        'application/pdf',
        'image/png',
        'image/jpeg',
        'text/plain'
    }

MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB

def is_attachment_safe(file):

    filename = file.filename.lower()
    _, ext = os.path.splitext(filename)

    # Check extension
    if ext not in ALLOWED_EXTENSIONS:
        return False

    # Check MIME type
    if file.mimetype not in ALLOWED_MIME_TYPES:
        return False

    # Check size
    file_content = file.read()
    if len(file_content) > MAX_FILE_SIZE:
        return False

    file.seek(0)  # Reset file pointer so file can still be read later
    return True

def attachment_check(attachments):

    attachment_score = 0.0
    attachment_message = ""

    unsafe_files = []

    if not attachments:
        return attachment_score, "No attachments found."

    for file in attachments:
        if not is_attachment_safe(file):
            unsafe_files.append(file.filename)

    if unsafe_files:
        attachment_score = 1.0
        attachment_message = f"Unsafe attachments found: {', '.join(unsafe_files)}"
    else:
        attachment_score = 0.0
        attachment_message = "Attachments seem safe."


    return attachment_score, attachment_message