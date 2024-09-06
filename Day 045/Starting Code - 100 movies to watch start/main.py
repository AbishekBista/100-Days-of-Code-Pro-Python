import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_data = response.text

soup = BeautifulSoup(movie_data, "html.parser")

all_movies = [title.getText() for title in soup.find_all(name="h3", class_="title")]

all_movies.reverse()

with open("movies.txt", mode="a", encoding="utf-8") as file:
    for movie in all_movies:
        file.write(f"{movie}\n")

        




