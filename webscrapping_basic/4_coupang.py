import requests
import re
from bs4 import BeautifulSoup

# connect Coupang (page 1 ~ page 5)
for i in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    page = requests.get(url,headers=headers)
    page.raise_for_status()

    soup = BeautifulSoup(page.content, "lxml")

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")}) # because of ad products
    for item in items:
        # except sponcer products
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            continue

        # except certain products
        name = item.find("div", attrs={"class": "name"}).get_text()
        if "HP" in name:
            continue

        # price
        price = item.find("strong", attrs={"class": "price-value"}).get_text()

        # grade
        grade = item.find("em", attrs={"class": "rating"})
        if grade:
            grade = grade.get_text()
        else:
            continue

        # review
        review = item.find("span", attrs={"class": "rating-total-count"})
        if review:
            review = review.get_text()
            review = review[1:-1] # except ()
        else:
            continue

        # link
        link = item.find("a", attrs={"class": "search-product-link"})["href"]

        if float(grade) >= 4.0 and int(review) >=100:
            print(f"name : {name}")
            print(f"price : {price}")
            print(f"evaluation : {grade} ({review})")
            print(f"URL : https://www.coupang.com{link}")
            print("-"*100)







