# parser.py - Functions for parsing PDF resumes and extracting text

import fitz

# Function to extract text from PDF using PyMuPDF (fitz)
def extract_text_from_pdf(file):
    try:
        with fitz.open(stream=file.file.read(), filetype="pdf") as pdf:
            text = ""
            
            for page in pdf:
                text += page.get_text()

        return text[:]

    except Exception as e:
        return f"Error reading PDF: {str(e)}"