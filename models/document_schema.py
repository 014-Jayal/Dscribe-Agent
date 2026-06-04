from pydantic import BaseModel
from typing import Optional


class PageContent(BaseModel):
    document_name: str
    page_number: int
    text: str
    document_type: Optional[str] = None


class DocumentBundle(BaseModel):
    patient_id: str
    pages: list[PageContent]