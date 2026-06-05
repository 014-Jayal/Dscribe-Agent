from tools.confidence import (
    calculate_confidence
)


def build_summary(

        extracted_data,

        sources,

        medication_changes,

        conflicts,

        interactions,

        review_flags

):

    enriched_data = {}

    for field, value in extracted_data.items():

        field_sources = sources.get(
            field,
            []
        )

        enriched_data[field] = {

            "value":
                value,

            "confidence":
                calculate_confidence(
                    value,
                    len(field_sources)
                ),

            "sources":
                field_sources
        }

    return {

        "clinical_summary":
            enriched_data,

        "medication_reconciliation":
            medication_changes,

        "conflicts":
            conflicts,

        "drug_interactions":
            interactions,

        "review_flags":
            review_flags
    }
