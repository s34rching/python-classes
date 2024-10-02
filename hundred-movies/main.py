from bs4 import BeautifulSoup
import requests

BASE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(BASE_URL)
source_html = response.text

soup = BeautifulSoup(source_html, "html.parser")
movie_elements = soup.select("h3.title")
movie_names = [element.getText() for element in movie_elements]
movie_names.reverse()

with open("./hundred-movies/movies.txt", mode="a") as movies_file:
    for movie in movie_names:
        movies_file.write(f"{movie},\n")
