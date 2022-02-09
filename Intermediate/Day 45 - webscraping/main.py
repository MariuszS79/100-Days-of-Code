from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = (response.text)

soup = BeautifulSoup(yc_web_page, "html.parser")

anchor_tag = (soup.find_all(name="a", class_="titlelink"))


linklist=[]

for i in anchor_tag:
    links = i.get("href")
    linklist.append(links)

print(*linklist, sep='\n')










# #import lxml
#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# #print(soup.find_all(name="a"))
#
# for tag in (soup.find_all(name="a")):
#     print(tag.get("href"))