import datetime
import requests
from bs4 import BeautifulSoup

class CinemaParser:
    def __init__(self, city = 'msk'):
        self.city = city

    def extract_raw_content(self):
        url = 'https://' + str(self.city) + '.subscity.ru/'
        answer = requests.get(url)
        self.content = BeautifulSoup(answer.text, 'html.parser')

    def print_raw_content(self):
        self.extract_raw_content()
        return self.content.prettify()

    def get_films_list(self):
        self.extract_raw_content()
        films = []
        prefilms = self.content.find_all("div", {"class": "movie-plate"})
        for prefilm in prefilms:
            films.append(prefilm["attr-title"])
        return films

    def get_film_nearest_session(self, movie_title):
        self.extract_raw_content()
        film = self.content.find("div", {"attr-title": movie_title})
        time = film["attr-next-screening"]
        screening_datetime = str(datetime.datetime.fromtimestamp(int(time)).strftime(
                '%Y-%m-%d %H:%M')).split()
        today = str(datetime.datetime.now()).split()
        if screening_datetime[0] == today[0]:
            href = film.find("a", {"class": "underdashed"})["href"]
            url = 'https://' + str(self.city) + '.subscity.ru' + str(href)
            page = BeautifulSoup(requests.get(url).text, "html.parser")
            trs = page.find_all("tr", {"class": "row-entity"})
            for i in range(len(trs)):
                td_i = trs[i].find("td", {"class": "text-center cell-screenings"})
                if str(td_i["attr-time"]) == str(time):
                    tr = trs[i]
                    cinema_name = tr.find("a", {"class": "underdashed"}).text
                    pass
            return(str(cinema_name), str(screening_datetime[1]))
        else:
            return(None, None)

