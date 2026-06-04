def find_source_pages(
        pages,
        extracted_text
):

    matches = []

    search_text = extracted_text[:50].lower()

    for page in pages:

        if search_text in page.text.lower():

            matches.append({
                "document":
                    page.document_name,

                "page":
                    page.page_number
            })

    return matches[:3]