import re

# Define keywords that indicate a non-academic affiliation
NON_ACADEMIC_KEYWORDS = ["Inc.", "Corp.", "Ltd.", "LLC", "Labs", "Company", "Technologies"]
EMAIL_PATTERNS = [r".*@.*(google|microsoft|ibm|amazon|facebook|apple)\.com"]

def is_academic_author(author_affiliation):
    """Check if an author is from an academic institution."""
    if not author_affiliation:  # Handle missing affiliation
        return True  # Assume academic if unknown

    if any(keyword in author_affiliation for keyword in NON_ACADEMIC_KEYWORDS):
        return False
    if any(re.match(pattern, author_affiliation) for pattern in EMAIL_PATTERNS):
        return False
    return True

def filter_academic_authors(papers):
    """Filter out non-academic authors based on affiliations."""
    for paper in papers:
        new_authors = []
        for author in paper.get("authors", []):
            affiliation = author.get("affiliation", "")  # Extract affiliation safely
            if is_academic_author(affiliation):
                new_authors.append(author["name"])  # Keep only name
        
        paper["authors"] = new_authors  # Update authors list
    return papers

if __name__ == "__main__":
    sample_papers = [
        {
            "id": "12345",
            "title": "Deep Learning in Medicine",
            "authors": [
                {"name": "Alice", "affiliation": "MIT"},
                {"name": "Bob", "affiliation": "Google"},
                {"name": "Charlie", "affiliation": "Harvard"}
            ],
            "source": "Nature",
            "pubdate": "2024-01-10"
        }
    ]
    filtered_papers = filter_academic_authors(sample_papers)
    print(filtered_papers)
