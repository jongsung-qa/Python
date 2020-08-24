import csv
import requests
from bs4 import BeautifulSoup

# url page에서 .format을 안쓰는 이유는 
# page가 맨뒤에 있기때문에 str으로 for문 돌려주면 되기 떄문
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# csv를 create
filename = "market capitalization(1 ~ 100).csv"
f = open(filename,"w",encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# title 찍기
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

# page1 ~ page2 
for page in range(1,3):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")

        # 의미없는 데이터 삭제
        if len(columns) <= 1:
            continue

        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)

