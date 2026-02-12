### This function search/scrape medical articles from https://pubmed.ncbi.nlm.nih.gov/ (Official website)
### Python version 3.8 compatible

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def pubmed_search(query: str):
    """
    Scrape PubMed search results for a query and return a list of
    dictionaries with title and link for each result item.
    """
    results = []
    
    # Encode query for URL
    query_encoded = quote(query)
    url = f"https://pubmed.ncbi.nlm.nih.gov/?term={query_encoded}"
    
    # Fetch the page
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Python Web Scraper)"
    }
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Error fetching PubMed page: HTTP {response.status_code}")
        return results

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all result items
    # On PubMed, results typically appear under <article> tags with class "full-docsum"
    for item in soup.find_all("article", class_="full-docsum"):
        title_tag = item.find("a", class_="docsum-title")
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = "https://pubmed.ncbi.nlm.nih.gov/" + title_tag["href"]
            results.append({"title": title, "link": link})
    
    return results

# Example usage
if __name__ == "__main__":
    search_term = "Headache"
    search_results = pubmed_search(search_term)
    
    for idx, result in enumerate(search_results, 1):
        print(f"{idx}. {result['title']}")
        print(f"   {result['link']}")


# Calling a function 
pubmed_search("Headache")
