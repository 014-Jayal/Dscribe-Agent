from doctor_simulator import doctor_edit
from reflector import generate_rule
from reward import similarity_score
from memory import save_rule, load_rules

with open(
    "outputs/patient_1_summary.txt",
    "r",
    encoding="utf-8"
) as f:
    original = f.read()

edited = doctor_edit(original)

score_before = similarity_score(
    original,
    edited
)

rule = generate_rule(
    original,
    edited
)

save_rule(rule)

rules = load_rules()

print("\n====================")
print("LEARNED RULE")
print("====================")
print(rule)

print("\n====================")
print("SIMILARITY SCORE")
print("====================")
print(score_before)

print("\n====================")
print("MEMORY")
print("====================")

for idx, r in enumerate(rules, start=1):
    print(f"{idx}. {r}")