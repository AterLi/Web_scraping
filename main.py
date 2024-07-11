from bs4 import BeautifulSoup
import requests

data = requests.get(
    url="https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
web_data = data.text

soup = BeautifulSoup(web_data, "html.parser")

all_titles = soup.find_all("h3", class_="title")
for i in all_titles[::-1]:
    movie = i.getText()
    with open(file="movies.txt", mode="a",  encoding='utf-8') as file:
        file.write(f"{movie}\n")
        print(movie)





