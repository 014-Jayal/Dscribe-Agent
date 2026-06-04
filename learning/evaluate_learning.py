from memory import load_rules

rules = load_rules()

print("\n===== LEARNED CLINICIAN PREFERENCES =====\n")

for i, rule in enumerate(rules, start=1):
    print(f"{i}. {rule}")