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
