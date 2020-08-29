from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import unittest

class FightBook(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://fly.interpark.com/")

    def test_reservation(self):

        # Departure
        dep = self.driver.find_element_by_id("dep_name")
        dep.clear()
        dep.send_keys("김포")
        time.sleep(2)
        dep.send_keys(Keys.ENTER)

        # Arrive
        arr = self.driver.find_element_by_id("arr_name")
        arr.clear()
        arr.send_keys("jeju")
        time.sleep(2)
        arr.send_keys(Keys.ENTER)

        # Date
        self.driver.find_element_by_id("depDateArrDate").click()
        time.sleep(2)
        self.driver.find_elements_by_link_text("31")[0].click()
        self.driver.find_element_by_xpath("//*[@id='section1']/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_elements_by_link_text("29")[0].click()
        self.driver.find_element_by_xpath("//*[@id='cal']/div/div[2]/a[1]").click()
        self.driver.find_element_by_class_name("ico-search").click()

        # 로딩시간 처리 : 드라이버를 통해서 브라우저를 최대 10초동안 기다리는데 뭔가 나오면 진행(10초 넘으면 에러 -> 그래서 try로 감싸줌)
        try:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='availDepResult']/table/tbody/tr[1]")))
            print(elem.text)
        except:
            print("no flight schedule")

        def tearDown(self):
            self.driver.quit()
                

if __name__ == "__main__":
    	unittest.main()
