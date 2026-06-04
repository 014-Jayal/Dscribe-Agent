# test_text.py

import fitz

doc = fitz.open("patient_data/patient 2 (1).pdf")

page = doc[0]

text = page.get_text()

print(len(text))

print(text[:1000])