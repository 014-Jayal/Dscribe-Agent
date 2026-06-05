from pathlib import Path

from tools.pdf_reader import extract_pdf_text


def load_patient_folder(folder_path):

    all_pages = []

    for pdf in Path(folder_path).glob("*.pdf"):

        pages = extract_pdf_text(str(pdf))

        all_pages.extend(pages)

    return all_pages
