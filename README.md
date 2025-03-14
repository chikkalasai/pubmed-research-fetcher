# PubMed Paper Fetcher and Academic Author Filter

This Python script fetches research papers from PubMed using the NCBI Entrez API based on a given query. It also filters authors to include only those affiliated with academic institutions.

## Features
- Fetches PubMed paper IDs using a search query.
- Retrieves paper details such as title, authors, source, and publication date.
- Filters out non-academic authors based on specific keywords and email patterns.

## Installation

### Prerequisites
Ensure you have Python 3.x installed on your system.

### Install Dependencies
Run the following command to install the required dependencies:

```sh
pip install requests


# PubMed Paper Fetcher and Academic Author Filter

This Python script fetches research papers from PubMed using the NCBI Entrez API based on a given query. It also filters authors to include only those affiliated with academic institutions.

## Features
- Fetches PubMed paper IDs using a search query.
- Retrieves paper details such as title, authors, source, and publication date.
- Filters out non-academic authors based on specific keywords and email patterns.

## Installation

### Prerequisites
Ensure you have Python 3.x installed on your system.

### Clone the Repository
Open a terminal or command prompt and run:

```sh
git clone https://github.com/chikkalasai/pubmed-research-fetcher.git
cd pubmed-research-fetcher/src
```

### Install Dependencies
Run the following command to install required dependencies:

```sh
pip install -r requirements.txt
```

## Usage
To fetch PubMed papers based on a query, run:

```sh
python -m papers_fetcher.cli "machine learning" -d
```

Replace `"machine learning"` with your desired search term.

Here in termianl we got output and 
The csv file saved on the your directoery
##The papera csv is in the directore
pubmed-research-fetcher/src/papers.csv

## Version Control
This project uses Git for version control. To push your changes:

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/chikkalasai/pubmed-research-fetcher.git
git push -u origin main
```

## External Tools & Libraries
- **Requests**: Used to make HTTP requests to the PubMed API.
- **Entrez API**: Fetches research papers from PubMed.

## License
This project is licensed under the MIT License.

## Contributions
Feel free to open an issue or submit a pull request to improve this project!




