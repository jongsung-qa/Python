import requests
from bs4 import BeautifulSoup

# 2015 ~ 2019 movie charts
for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    page = requests.get(url, headers=headers)
    page.raise_for_status()

    soup = BeautifulSoup(page.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})
    
    for idx, image in enumerate(images):
        img_url = image["src"]
        if img_url.startswith("//"):
            img_url = "http:" + img_url
        image_res = requests.get(img_url)
        page.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4:
            break