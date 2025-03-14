import requests
import csv
import argparse
import sys
import json

# Function to fetch papers from the API based on a search query
def fetch_papers(query):
    url = f"https://api.example.com/search?query={query}&format=json"  # Replace with actual API URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)
    
    data = response.json()
    
    # Example: Assuming 'data' contains a list of papers under a 'papers' key
    papers = data.get('papers', [])
    
    return papers

# Function to save the fetched papers to a CSV file
def save_to_csv(papers, filename='papers.csv'):
    # Define the header for the CSV
    header = ['title', 'authors', 'journal', 'year']
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        
        for paper in papers:
            # Extract relevant fields from the paper (with default 'N/A' if missing)
            title = paper.get('title', 'N/A')
            authors = ', '.join([author.get('name', 'N/A') for author in paper.get('authors', [])])
            journal = paper.get('journal', 'N/A')
            year = paper.get('year', 'N/A')
            
            # Write the data to the CSV
            writer.writerow({
                'title': title,
                'authors': authors,
                'journal': journal,
                'year': year
            })

# Main function to handle CLI arguments and invoke necessary functions
def main():
    parser = argparse.ArgumentParser(description="Fetch papers and save to CSV")
    
    # Adding arguments for the search query and the flag for saving data
    parser.add_argument('query', type=str, help="Search query for fetching papers")
    parser.add_argument('-d', '--download', action='store_true', help="Flag to download the papers and save to CSV")
    
    # Parse the arguments
    args = parser.parse_args()

    # Fetch papers based on the query
    print(f"Fetching papers for query: {args.query}")
    papers = fetch_papers(args.query)

    # If the download flag is set, save the papers to a CSV file
    if args.download:
        print("Saving papers to CSV...")
        save_to_csv(papers)
        print("Papers saved successfully.")
    else:
        # Otherwise, just print the fetched papers (for debugging or simple output)
        for paper in papers:
            print(f"Title: {paper.get('title', 'N/A')}")
            print(f"Authors: {', '.join([author.get('name', 'N/A') for author in paper.get('authors', [])])}")
            print(f"Journal: {paper.get('journal', 'N/A')}")
            print(f"Year: {paper.get('year', 'N/A')}")
            print("-" * 80)

# If this file is being run as a script, invoke the main function
if __name__ == '__main__':
    main()
