# Metadata Extractor Python

Python utility that extracts metadata from DOCX, PDF and JPG/JPEG files.

## Features
- File selection using Tkinter
- DOCX metadata extraction
- PDF metadata extraction
- JPG/JPEG EXIF metadata extraction
- JSON output in the terminal
- Basic file validation

## Technologies Used
- Python
- Tkinter
- PyPDF2
- exifread
- Pillow
- python-docx
- JSON

## Supported File Types
- `.docx`
- `.pdf`
- `.jpg`
- `.jpeg`

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python metadata_extractor.py
   ```
3. Select a supported file from the file dialog.
4. Check the extracted metadata in the terminal.

## Example Output
```json
{
  "Title": "Example document",
  "Author": "User",
  "Created": "2025-01-01 10:00:00",
  "Modified": "2025-01-02 12:00:00"
}
```
