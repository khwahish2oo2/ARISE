from fastapi import UploadFile, File
import PyPDF2
import os

def extract_text_func(file: UploadFile = File(...)):
    if not os.path.exists("new_uploads"):
        os.makedirs("new_uploads")
    file_path = os.path.join("new_uploads", file.filename)

    with open(file_path, "wb") as pdf_file:
            pdf_file.write(file.file.read())

    with open(file_path, "rb") as path:
        pdf_reader = PyPDF2.PdfReader(file_path)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    return text