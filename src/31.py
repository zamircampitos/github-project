import requests
from bs4 import BeautifulSoup

def get_html_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while getting the HTML data: {e}")
        return None

def parse_html(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    # Add your code here to parse and process the HTML data
    # For example, you can extract text from the parsed HTML
    pass

if __name__ == "__main__":
    url = "https://example.com"
    html_data = get_html_data(url)
    
    if html_data:
        soup = BeautifulSoup(html_data, 'html.parser')
        parse_html(soup)
