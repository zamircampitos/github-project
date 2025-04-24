import random
import requests
from bs4 import BeautifulSoup

def get_random_movie():
    url = "https://www.imdb.com/chart/toptv/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    movies = soup.find('div', {'class': 'lister-list'}).find_all('td', {'class': 'titleColumn'})
    
    movie_data = [movie.text for movie in movies]
    random_movie = random.choice(movie_data)
    
    return f"The randomly selected movie is {random_movie}."
