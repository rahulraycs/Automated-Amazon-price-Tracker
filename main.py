import requests
from bs4 import BeautifulSoup
import lxml

import smtplib



URL="https://www.amazon.in/boAt-BassHeads-100-Headphones-Black/dp/B071Z8M4KX/ref=sr_1_3?dchild=1&keywords=HEADPHONES+BOAT&qid=1623314551&sr=8-3"

response= requests.get(URL ,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9",
})
soup=BeautifulSoup(response.text,"lxml")
price=soup.find(name="span",class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()

price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency)
print(price_as_float)




title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("rahulray2103@gmail.com", "Rahul210397*")

        connection.sendmail(
            from_addr="rahulray2103@gmail.com",
            to_addrs="rahulray2103@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )




