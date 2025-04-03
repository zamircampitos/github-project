import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Error: Unable to retrieve data from the URL.")
        return None

url = "https://www.example.com"
html_content = fetch_html(url)
if html_content:
    soup = BeautifulSoup(html_content, 'html.parser')
    # Add your code here, e.g., extract information or perform calculations
    # For example:
    # print(soup.title.text)
    # print(soup.prettify())
