import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

html_content = fetch_html("https://www.example.com")

if html_content is not None:
    soup = BeautifulSoup(html_content, "html.parser")
    # Example code to extract data from the HTML content (for demonstration purposes only)
    data = soup.find_all(class_="some-class")
    print(data)  # This part depends on your specific needs
else:
    print("Failed to fetch the webpage.")
