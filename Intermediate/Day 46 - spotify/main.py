from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')

raw_songs = soup.find_all(name='h3', class_='a-no-trucate', id="title-of-a-story")
artist_name = soup.select(".c-label.a-font-primary-s")

song_titles = [songs.getText().replace('\n', '') for songs in raw_songs]
artiste = [artist.getText().replace('\n', '') for artist in artist_name]

zipped = zip(song_titles, artiste)

for i in zipped:
    print(i)