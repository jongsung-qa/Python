from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://www.skyscanner.co.kr/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
#res = requests.get(url, headers=headers)  # 403
#res.raise_for_status()

browser.get(url)

# 출발지 선택
departure = browser.find_element_by_id("fsc-origin-search")
departure.send_keys("Incheon")
departure.send_keys(Keys.ENTER)

# 도착지 선택
departure = browser.find_element_by_id("fsc-destination-search")
departure.send_keys("Toronto Pearson")
departure.send_keys(Keys.ENTER)

# 가는날 선택
browser.find_element_by_id("depart-fsc-datepicker-button").click()
browser.find_element_by_xpath("//*[@id='depart-fsc-datepicker-popover']/div/div/div[2]/div/table/tbody/tr[5]/td[7]/button/span").click()

# 오는 날짜 선택
browser.find_element_by_id("return-fsc-datepicker-button").click()
browser.find_element_by_xpath("//*[@id='return-fsc-datepicker-popover']/div/div/div[2]/div/table/tbody/tr[5]/td[3]/button/span").click()

# 항공권 검색
browser.find_element_by_xpath("//*[@id='flights-search-controls-root']/div/div/form/div[3]/button").click()

# 로딩시간 처리
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='app-root']/div[1]/div/div[2]/div[2]/div[1]/div[4]/div[1]/div/div/a/div")))
    print(elem.text)
finally:
    browser.quit()
