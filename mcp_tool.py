from mcp.server.fastmcp import FastMCP
from functions.symptoms_extractor import symptoms_extractor
from functions.symptoms_diagnosis import symptoms_diagnosis
from functions.pubmed_search import pubmed_search
from functions.summarize_text import summarize_text

# Init MCP
mcp=FastMCP("Medical Diagnosis AI App")

async def medical_diagnosis_ai_app(symptom_text):
    symptoms=symptoms_extractor(symptom_text)
    diagnosis_result=symptoms_diagnosis(symptoms)
    pubmed_article=pubmed_search(" ".join(symptoms))  
    summary=summarize_text(pubmed_article[:3000])   

    return{
        "symptoms":symptoms,
        "diagnosis":diagnosis_result,
        "summary":summary
    }

if __name__ =="__main__":
    mcp.run(transport="stdio")

