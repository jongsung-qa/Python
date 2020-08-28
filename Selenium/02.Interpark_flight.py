from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://fly.interpark.com/"
browser.get(url)

# Departure
dep = browser.find_element_by_id("dep_name")
dep.clear()
dep.send_keys("김포")
time.sleep(2)
dep.send_keys(Keys.ENTER)

# Arrive
arr = browser.find_element_by_id("arr_name")
arr.clear()
arr.send_keys("jeju")
time.sleep(2)
arr.send_keys(Keys.ENTER)

# Date
browser.find_element_by_id("depDateArrDate").click()
time.sleep(2)
browser.find_elements_by_link_text("30")[0].click()
browser.find_element_by_xpath("//*[@id='section1']/div[2]/button[2]").click()
time.sleep(1)
browser.find_elements_by_link_text("29")[0].click()
browser.find_element_by_xpath("//*[@id='cal']/div/div[2]/a[1]").click()
browser.find_element_by_class_name("ico-search").click()

# 로딩시간 처리 : 드라이버를 통해서 브라우저를 최대 10초동안 기다리는데 뭔가 나오면 진행(10초 넘으면 에러 -> 그래서 try로 감싸줌)
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='availDepResult']/table/tbody/tr[1]")))
    print(elem.text)
finally:
    browser.quit()
