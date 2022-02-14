import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 30

url = "https://www.amazon.co.uk/dp/B07JQRYR5M/ref=pav_d_fromAsin_B0839NDV5D_toAsin_B07JQRYR5M"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.82 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

title = soup.find(id="productTitle").get_text().strip()

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("£")[1]
price_float = float(price_without_currency)

if price_float < BUY_PRICE:
    message = f"Bargain! {title} is now {price}"

    with smtplib.SMTP(smtp.gmail.com, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )