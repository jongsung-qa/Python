from selenium import webdriver
#from selenium.webdriver.common.key import keys
#import time

browser = webdriver.Chrome()
# Move to amazon
browser.get("https://www.amazon.ca/")

# TC1
signin = browser.find_element_by_id("nav-link-accountList")
signin.click()
create = browser.find_element_by_id("createAccountSubmit").click()
print("Success TC1")

# TC2
name = browser.find_element_by_name("customerName").send_keys("jongsung")
email = browser.find_element_by_name("email").send_keys("baelong21@naver.com")
passward = browser.find_element_by_name("password").send_keys("abcde123")
repassward = browser.find_element_by_name("passwordCheck").send_keys("fihjk456")
print("Success TC2")

# TC3 & TC4
Create = browser.find_element_by_id("continue")
alert = browser.find_element_by_class_name("a-alert-content")
if alert:
    browser.find_element_by_name("passwordCheck").clear() #필드삭제
    browser.find_element_by_name("passwordCheck").send_keys("abcde123")
print("Success TC3&4")

# TC5
Create = browser.find_element_by_id("continue")
print("Success TC5")

# Exit current tab only
# browser.close()  

# Exit full tab
browser.quit()  # 전체 브라우저 종료
