import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to load page at {url}")

html = fetch_html("https://example.com")
soup = BeautifulSoup(html, "html.parser")

# Example: find all <h1> tags and print their text
for tag in soup.find_all("h1"):
    print(tag.text)

# Example: get the title of the first paragraph
paragraph = soup.find("p", {"class": "my-class"})
print(paragraph.get_text())
