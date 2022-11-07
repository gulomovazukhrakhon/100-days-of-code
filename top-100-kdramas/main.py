from bs4 import BeautifulSoup
import requests


def top_korean_dramas(url):
    response = requests.get(url)
    contents = response.text
    soup = BeautifulSoup(contents, "html.parser")

    # Getting Titles

    movie_lists = soup.select(selector='h6 a')
    movie_titles = [movie.getText() for movie in movie_lists[::2]]

    # Getting the Rates

    movie_rate_lists = soup.find_all(name='span', class_="p-l-xs score")
    movie_rates = [rate.getText() for rate in movie_rate_lists]

    return movie_titles, movie_rates

for page in range(1, 6):
    URL = f"https://mydramalist.com/shows/top_korean_dramas?page={page}"

    titles, rates = top_korean_dramas(url=URL)

    print(titles, rates)
