from pathlib import Path

from tools.pdf_reader import extract_pdf_text

pdfs = list(
    Path("patient_data").glob("*.pdf")
)

print(pdfs)

pages = extract_pdf_text(
    str(pdfs[0])
)

print(
    pages[0].text[:500]
)