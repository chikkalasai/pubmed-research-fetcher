import requests
import json
import time  # Added delay for API rate limits

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
DATABASE = "pubmed"

def fetch_paper_ids(query, max_results=10):
    """Fetches PubMed paper IDs based on the query."""
    params = {
        "db": DATABASE,
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    if not paper_ids:
        print("No papers found for the given query.")
        return []
    
    return paper_ids

def fetch_paper_details(paper_ids):
    """Fetches detailed information about the papers using their IDs."""
    if not paper_ids:
        return []

    params = {
        "db": DATABASE,
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    
    time.sleep(1)  # Prevent API rate limit issues
    response = requests.get(DETAILS_URL, params=params)
    response.raise_for_status()
    data = response.json()

    print("\n✅ DEBUG: Raw API Response:")
    print(json.dumps(data, indent=4))  # Debugging: Print full API response

    papers = []
    for paper_id in paper_ids:
        if paper_id in data["result"]:
            paper_info = data["result"][paper_id]

            title = paper_info.get("title", "Unknown")

            # Fixing journal extraction
            journal = paper_info.get("fulljournalname", paper_info.get("source", "Unknown"))

            # Fixing year extraction (extracting only the year from pubdate)
            pubdate = paper_info.get("pubdate", "Unknown")
            year = pubdate.split()[0] if pubdate != "Unknown" else "Unknown"

            url = f"https://pubmed.ncbi.nlm.nih.gov/{paper_id}/"

            papers.append({
                "id": paper_id,
                "title": title,
                "authors": [
                    {"name": author.get("name", "Unknown"), "affiliation": author.get("affiliation", "")}
                    for author in paper_info.get("authors", [])
                ],
                "journal": journal,  # ✅ Fixed journal mapping
                "year": year,        # ✅ Fixed year extraction
                "url": url
            })

    print("\n✅ DEBUG: Extracted Data:")
    for paper in papers[:5]:  # Print first 5 for debugging
        print(json.dumps(paper, indent=4))

    return papers

if __name__ == "__main__":
    query = "machine learning"
    paper_ids = fetch_paper_ids(query)
    papers = fetch_paper_details(paper_ids)
