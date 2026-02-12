import re
from typing import List  # for python 3.8 
def symptoms_extractor(text: str) -> List[str]: #List is for python 3.8
    symptoms = re.findall(r"\b(fever|headache|fatigue)\b", text.lower())
    return list(set(symptoms))  # remove duplicates

text = "I have been experiencing fever and headache for 3 days"
symptoms = symptoms_extractor(text)
print(symptoms)
