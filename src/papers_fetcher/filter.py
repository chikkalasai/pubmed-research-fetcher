import argparse
import csv
from fetch import fetch_paper_ids, fetch_paper_details
from filter import filter_academic_authors

def save_to_csv(papers):
    with open("papers.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "authors", "journal", "year", "url"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for paper in papers:
            title = paper.get("title", "Unknown")
            authors = ", ".join([author.get("name", "Unknown") for author in paper.get("authors", [])])
            journal = paper.get("journal", "Unknown")
            year = paper.get("year", "Unknown")
            url = paper.get("url", "Unknown")

            print(f"DEBUG: {title}, {authors}, {journal}, {year}, {url}")  # Debug print

            writer.writerow({
                "title": title,
                "authors": authors,
                "journal": journal,
                "year": year,
                "url": url
            })

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter PubMed research papers.")
    parser.add_argument("query", type=str, help="Search query for PubMed articles.")
    parser.add_argument("-d", "--download", action="store_true", help="Save results to a CSV file.")
    parser.add_argument("-f", "--filter", action="store_true", help="Filter non-academic authors.")

    args = parser.parse_args()
    
    print(f"Fetching papers for query: {args.query}")
    paper_ids = fetch_paper_ids(args.query)
    if not paper_ids:
        print("No papers found. Try a different query.")
        return
    
    papers = fetch_paper_details(paper_ids)
    if not papers:
        print("No detailed results found. Check your API response.")
        return

    if args.filter:
        print("Filtering non-academic authors...")
        papers = filter_academic_authors(papers)

    if args.download:
        save_to_csv(papers)
        print(f"Results saved to papers.csv")
    else:
        for paper in papers:
            authors = [author["name"] if isinstance(author, dict) and "name" in author else str(author) for author in paper["authors"]]
            print(f"Title: {paper['title']}\nAuthors: {', '.join(authors)}\nJournal: {paper['journal']}\nYear: {paper['year']}\nURL: {paper['url']}\n")

if __name__ == "__main__":
    main()
