# import os 
# from dotenv import load_dotenv
# import openai
# from typing import List

# load_dotenv()

# client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# def symptoms_diagnosis(symptoms:List[str]) -> str:
#     prompt=f"Patient has symptoms: {','.join(symptoms)}.Suggest possible medical diagnosis and suggest me a possible cure"

#     response=client.chat.completions.create(
#         model="gpt-4",
#         messages=[
#             {"role":"system","content":"You are a helpful medical assistant"},
#             {"role":"user","content":prompt}
#         ]
#     )
#     return response.choices[0].message.content.strip()


# # testing 
# output = symptoms_diagnosis(["fever","headache"])
# print(output) 



# Since my pyton version is 3.8, the below code is compatible with 3.8 version and with openai 
import os
from dotenv import load_dotenv
import openai
from typing import List  # Needed for Python 3.8 type hints

# Load environment variables from .env
load_dotenv()

# Set the API key for openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def symptoms_diagnosis(symptoms: List[str]) -> str:
    """
    Takes a list of symptoms and returns a possible diagnosis and suggestion
    using OpenAI GPT-4.
    """
    prompt = f"Patient has symptoms: {', '.join(symptoms)}. Suggest possible medical diagnosis and possible cure."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return the assistant's message
    return response.choices[0].message["content"].strip()

# Testing
if __name__ == "__main__":
    output = symptoms_diagnosis(["fever", "headache"])
    print(output)
