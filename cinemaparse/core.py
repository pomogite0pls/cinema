import requests
from bs4 import BeautifulSoup

class CinemaParser:
    def __init__(self, city):
        self.city = city

    def extract_raw_content(self):
        url = 'https://' + str(self.city) + '.subscity.ru/'
        answer = requests.get(url)
        self.content = BeautifulSoup(answer.text, 'html.parser')

    def print_raw_content(self):
        return self.content.prettify()

    def get_films_list(self):
        films = []
        prefilms = self.content.find_all("div", {"class": "movie-plate"})
        for prefilm in prefilms:
            films.append(prefilm["attr-title"])
        return films
