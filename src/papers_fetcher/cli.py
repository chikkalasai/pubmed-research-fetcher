import argparse
import csv
from papers_fetcher.fetch import fetch_paper_ids, fetch_paper_details
from papers_fetcher.filter import filter_academic_authors

def save_to_csv(papers):
    with open("papers.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
        fieldnames = ["title", "authors", "journal", "year", "url"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for paper in papers:
            title = paper.get("title", "Unknown")
            
            # Ensure authors are extracted properly
            authors_list = paper.get("authors", [])
            if isinstance(authors_list, list):
                authors = ", ".join([author.get("name", "Unknown") for author in authors_list])
            else:
                authors = "Unknown"
                
            journal = paper.get("journal", "Unknown")
            year = paper.get("year", "Unknown")
            url = paper.get("url", "Unknown")

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

    # Debugging: Print sample data
    print("\n✅ Sample Output:")
    for paper in papers[:3]:  # Print only first 3 for checking
        print(paper)

    if args.filter:
        print("Filtering non-academic authors...")
        papers = filter_academic_authors(papers)

    if args.download:
        save_to_csv(papers)
        print(f"✅ Results saved to papers.csv")
    else:
        for paper in papers:
            title = paper.get("title", "Unknown")
            authors = [author["name"] if isinstance(author, dict) and "name" in author else str(author) for author in paper.get("authors", [])]
            journal = paper.get("journal", "Unknown")
            year = paper.get("year", "Unknown")
            url = paper.get("url", "Unknown")

            print(f"\n📌 Title: {title}")
            print(f"👨‍🔬 Authors: {', '.join(authors)}")
            print(f"📖 Journal: {journal}")
            print(f"📅 Year: {year}")
            print(f"🔗 URL: {url}\n")

if __name__ == "__main__":
    main()
