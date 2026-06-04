import json


def extract_medication_list(extracted_json):

    try:

        data = json.loads(
            extracted_json
        )

        return data.get(
            "medications",
            []
        )

    except:

        return []