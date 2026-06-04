import fitz
import pytesseract
from pathlib import Path
from PIL import Image

from models.document_schema import PageContent

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def ocr_page(page):

    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

    img = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
        pix.samples
    )

    text = pytesseract.image_to_string(img)

    return text


def extract_pdf_text(pdf_path):

    pages = []

    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):

        page = doc[page_num]

        text = page.get_text()

        if len(text.strip()) < 30:
            text = ocr_page(page)

        pages.append(
            PageContent(
                document_name=Path(pdf_path).name,
                page_number=page_num + 1,
                text=text
            )
        )

    return pages