# Wikipedia Page Web Scrapper

# Project Overview
This repository contains a Python-based prototype for data extraction and analysis of members of the 17th Lok Sabha in India. The project utilizes web scraping techniques to gather information from Wikipedia, focusing on extracting details such as constituency, name, party affiliation, and relevant hyperlinks of members. Additionally, the project lays the groundwork for future extensions aimed at analyzing relationships and contexts surrounding these members, which could further enhance understanding of the political landscape.

# How Does This Prototype Work?
1. Data Extraction using india.py

Web Scraping: The script uses the requests library to retrieve the webpage containing the list of members of the 17th Lok Sabha.
HTML Parsing: The BeautifulSoup library is employed to parse the HTML content and extract data from tables.
Data Structuring: Extracted data, including constituency, name, party, and hyperlinks, is organized into a list of dictionaries.
CSV Export: Finally, the structured data is saved to a CSV file for easy access and analysis.

2. Text Processing and Relationship Extraction using relationship.py

Text Extraction: The script retrieves textual content from a specific Wikipedia page and cleans it using BeautifulSoup.
Natural Language Processing: The spaCy library is used to analyze the extracted text, breaking it down into sentences for potential further processing and analysis.
Content Evaluation: The extracted sentences can serve as input for deeper analyses, such as identifying relationships among members based on their biographies and public information.

# Methodology
1. Initialization:

Import necessary libraries: requests, spacy, csv, and BeautifulSoup.
Load the English NLP model using spaCy.

2. Data Extraction:

Use requests to fetch data from the Wikipedia page of the 17th Lok Sabha.
Parse the page using BeautifulSoup to locate and extract relevant information.

3. Data Structuring:

Organize the scraped data into a list of dictionaries.
Handle variations in table structures (e.g., rowspan attributes) to ensure accurate data extraction.

4. CSV Export:

Write the structured data into a CSV file for easy manipulation and analysis.

![image](https://github.com/user-attachments/assets/73493330-da9f-4629-8a3b-ffe0925f28ed)


# Challenges Faced and Solutions
1. Inconsistent Table Structures:

Problem: Different rows in the tables had varying numbers of columns.

Solution: Implement conditional checks to handle different structures and extract data accordingly.

2. Data Cleanliness:

Problem: Retrieved text contained unnecessary HTML tags and comments.

Solution: Utilize a filtering function to extract only visible text, improving data quality.

3. Web Scraping Limitations:

Problem: Frequent changes to the Wikipedia layout can break the scraper.

Solution: Regularly update the code to adapt to changes in HTML structure.

# Key Features
1. Automated Data Extraction: Efficiently scrapes and structures data from the Wikipedia page.
2. Natural Language Processing Integration: Leverages spaCy for advanced text analysis capabilities.
3. CSV Output: Exports cleaned and structured data for easy access and further analysis.

# Future Work
In future iterations of this project, additional functionalities will be implemented to enhance the depth and breadth of analysis regarding the members of the 17th Lok Sabha:

1. Relationship Mapping: Extend the functionality to analyze relationships between members based on shared constituencies, party affiliations, and political history. The existing relationship.py script can be modified to include algorithms that identify and visualize connections among members.

2. Sentiment Analysis: Utilize NLP techniques to analyze public sentiments about each member by scraping additional data from news articles and social media platforms.

3. Enhanced Data Visualization: Develop visual representations of the collected data, such as graphs and charts, to provide insights into party distributions, constituency representation, and member activity.

4. Broader Data Sources: Incorporate data from other platforms, including government websites and news articles, to create a comprehensive database for political analysis.

5. Real-Time Updates: Implement a scheduling mechanism to regularly update the data extracted from Wikipedia and other sources to ensure the analysis remains current.
