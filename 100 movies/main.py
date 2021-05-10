from bs4 import BeautifulSoup
import requests

URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")


all_movies = soup.find_all("a", "title")

print(all_movies)

