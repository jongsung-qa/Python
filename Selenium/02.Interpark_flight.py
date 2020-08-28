from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://fly.interpark.com/"
browser.get(url)

# Departure
dep = browser.find_element_by_id("dep_name")
dep.clear()
dep.send_keys("toronto")
dep.send_keys(Keys.ENTER)

# Arrive
arr = browser.find_element_by_id("arr_name")
arr.clear()
arr.send_keys("Incheon")
arr.send_keys(Keys.ENTER)

# Date
browser.find_element_by_id("depDateArrDate").click()

browser.find_elements_by_link_text("31")[0].click()
browser.find_elements_by_link_text("31")[1].click()
