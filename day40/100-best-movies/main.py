import requests
from bs4 import BeautifulSoup
movie_endpoint = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=movie_endpoint)
response.raise_for_status()
response_data = response.text
contents = BeautifulSoup(response_data, "html.parser")
# title = contents.select()
# title = contents.find_all(name="h3", class_="jsx-4245974604")
print(contents)
