import requests
from bs4 import BeautifulSoup
import re

def extract_and_process_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract and process specific text here
    # Example: Extract all HTML tags containing the word "school"
    html_tags = soup.find_all('h1', {'class': 'school-name'})
    for tag in html_tags:
        print(tag.text.strip())

def main():
    url = 'https://example.com/schools'  # Replace with your desired URL
    extract_and_process_text(url)
    
if __name__ == "__main__":
    main()
