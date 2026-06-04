# debug_patient.py

from tools.patient_loader import load_patient_folder

pages = load_patient_folder("patient_data")

for page in pages[:10]:

    print("\n" + "="*80)
    print(page.page_number)
    print("="*80)

    print(page.text[:3000])