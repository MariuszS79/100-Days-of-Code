from bs4 import BeautifulSoup
#import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#print(soup.find_all(name="a"))

for tag in (soup.find_all(name="a")):
    print(tag.get("href"))l