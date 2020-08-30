# 네이버 항공권 검색
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 로딩 처리를 위한 import
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

browser = webdriver.Chrome()
browser.maximize_window() # browser 창 최대화

url = "http://flight.naver.com/flights"
browser.get(url)

# 출발지 선택
dep2 = browser.find_element_by_xpath("//*[@id='l_1']/div/div[1]/a[2]")
dep2.click().send_key("toronto")
dep1.send_keys("toronto")
dep.send_keys(Keys.ENTER)

dep3 = browser.find_element_by_class_name(
    "inp_airport selectAutocomplete ng-pristine ng-valid").send_Keys("toronto")

# 항공권 검색
search = browser.find_element_by_id("query")
search.send_keys("네이버항공권")
search.send_keys(Keys.ENTER)


# 가는날 선택
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27,28일 선택(주의:elements)
#browser.find_elements_by_link_text("27")[0].click() # [0] 이번달 27일 선택
#browser.find_elements_by_link_text("28")[0].click()  # [0] 이번달 27일 선택

# 다음달 27,28일 선택(주의:elements)
browser.find_elements_by_link_text("27")[1].click() # [1] 다음달 27일 선택
browser.find_elements_by_link_text("28")[1].click()  # [1] 다음달 27일 선택

# 제주도 선택 (xpath 할때는 따옴표 주의)
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 로딩시간 처리 : 드라이버를 통해서 브라우저를 최대 10초동안 기다리는데 뭔가 나오면 진행(10초 넘으면 에러 -> 그래서 try로 감싸줌)
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
finally:
    browser.quit()

# 첫번째 결과 출력
#elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
#print(elem.text)
