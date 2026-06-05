def find_sources(
        pages,
        extracted_data
):

    sources = {}

    for field, value in extracted_data.items():

        if value in [
            None,
            "",
            [],
            "NOT_FOUND"
        ]:
            continue

        sources[field] = []

        if isinstance(value, list):

            search_terms = [
                str(item).lower()[:20]
                for item in value
            ]

        else:

            search_terms = [
                str(value).lower()[:20]
            ]

        for page in pages:

            page_text = page.text.lower()

            for term in search_terms:

                if term and term in page_text:

                    sources[field].append({

                        "document":
                            page.document_name,

                        "page":
                            page.page_number
                    })

                    break

        sources[field] = (
            sources[field][:3]
        )

    return sources
