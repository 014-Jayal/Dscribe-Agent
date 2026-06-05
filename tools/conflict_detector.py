import json
import re
from config.gemini import llm

CONFLICT_PROMPT = """
You are a Medical Safety Agent. Your job is to detect clinical contradictions.

Review the 'Extracted Data' against the 'Clinical Notes Context' provided below.
Look specifically for:
1. Diagnoses mentioned in the raw notes that contradict or drastically differ from the extracted principal diagnosis.
2. Severe mismatches in the patient's narrative or condition.

Extracted Data:
{extracted_data}

Clinical Notes Context:
{context}

Return ONLY a JSON list of strings detailing the conflicts. If there are no conflicts, return an empty list [].
Example: ["Discharge note lists Gastroenteritis, but consultation note lists DKA."]
"""

def detect_conflicts(extracted_data, context_text):
    try:
        response = llm.invoke(CONFLICT_PROMPT.format(
            extracted_data=json.dumps(extracted_data),
            context=context_text[:15000] # Kept within strict context limits
        ))
        
        text = response.content.replace("```json", "").replace("```", "").strip()
        
        # Regex fallback to ensure we capture the list
        match = re.search(r'\[.*\]', text, re.DOTALL)
        if match:
            conflicts = json.loads(match.group(0))
        else:
            conflicts = json.loads(text)
            
        if isinstance(conflicts, list):
            return conflicts
        return []
        
    except Exception as e:
        print(f"Conflict detection error: {e}")
        return ["System Error: Could not run advanced conflict detection. Clinician must manually cross-reference notes."]
