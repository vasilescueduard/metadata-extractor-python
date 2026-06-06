import os
import sys
import json
import exifread
import PyPDF2
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from docx import Document

def extract_metadata_docx(file_path):
    doc = Document(file_path)
    props = doc.core_properties
    metadata = {
        "Title": props.title,
        "Author": props.author,
        "Created": props.created,
        "Modified": props.modified,
        "Keywords": props.keywords,
        "Comments": props.comments,
    }
    return metadata

def extract_metadata_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        metadata = reader.metadata
    return dict(metadata) if metadata else {}

def extract_metadata_jpg(file_path):
    with open(file_path, "rb") as f:
        tags = exifread.process_file(f)
    return {tag: str(value) for tag, value in tags.items()}

def extract_metadata(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".docx":
        return extract_metadata_docx(file_path)
    elif ext == ".pdf":
        return extract_metadata_pdf(file_path)
    elif ext in [".jpg", ".jpeg"]:
        return extract_metadata_jpg(file_path)
    else:
        return {"Error": "Format not suportat"}

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selectează un fișier",
                                           filetypes=[("Documente", "*.docx;*.pdf;*.jpg;*.jpeg"),
                                                      ("Toate fișierele", "*.*")])
    return file_path

def main():
    file_path = select_file()
    if not file_path:
        print("Niciun fișier selectat!")
        return
    if not os.path.exists(file_path):
        print("Fișierul nu există!")
        return
    metadata = extract_metadata(file_path)
    print(json.dumps(metadata, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
