from cinemaparse import CinemaParser

msk_parser = CinemaParser()
print(msk_parser.print_raw_content())
print(msk_parser.get_films_list())
print(msk_parser.get_film_nearest_session("Джокер"))
print(msk_parser.get_film_nearest_session("Портрет девушки в огне"))

