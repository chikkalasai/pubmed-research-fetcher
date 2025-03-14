import argparse
import csv
from papers_fetcher.fetch import fetch_paper_ids, fetch_paper_details
from papers_fetcher.filter import filter_academic_authors

def save_to_csv(papers, filename="papers.csv"):
    """Save paper details to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "authors", "source", "pubdate"])
        writer.writeheader()
        for paper in papers:
            writer.writerow({
                "id": paper["id"],
                "title": paper["title"],
                "authors": ", ".join(paper["authors"]),
                "source": paper["source"],
                "pubdate": paper["pubdate"]
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
            print(f"Title: {paper['title']}\nAuthors: {', '.join(paper['authors'])}\nSource: {paper['source']}\nPub Date: {paper['pubdate']}\n")

if __name__ == "__main__":
    main()
