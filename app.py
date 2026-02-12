from fastapi import FastAPI 
from pydantic import BaseModel
from functions.symptoms_extractor import symptoms_extractor
from functions.symptoms_diagnosis import symptoms_diagnosis
from functions.pubmed_search import pubmed_search
from functions.summarize_text import summarize_text

# Init fastapi 
app = FastAPI() 

class SymptomInput(BaseModel):
    description: str 

@app.post("/diagnosis") # define endpoint of app with route diagnosis
def diagnosis(data:SymptomInput):
    symptoms=symptoms_extractor(data.description)
    diagnosis_result=symptoms_diagnosis(symptoms)
    pubmed_article=pubmed_search(" ".join(symptoms))  # passing the list of symptoms
    summary=summarize_text(pubmed_article[:3000])   #3000 discussions or statments
    
    return{
        "symptoms":symptoms,
        "diagnosis":diagnosis_result,
        "summary":summary
    }

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("app:app",host="0.0.0.0",port=8080,reload=True)
    # file name (app.py):fastapi object name (app = FastAPI())