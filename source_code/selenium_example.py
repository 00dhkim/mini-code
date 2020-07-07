import time
from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")


driver.get("http://lms.knu.ac.kr")

login_btn = driver.find_element_by_xpath("//div[@class='header_login_img']")
login_btn.click()
driver.implicitly_wait(10)

driver.find_element_by_id("usr_id").send_keys("ID")
driver.find_element_by_id("usr_pwd").send_keys("PASSWORD")
driver.find_element_by_id("login_btn").click()
time.sleep(1)

driver.switch_to.alert.accept()
driver.get("http://lms.knu.ac.kr")

logo = driver.find_element_by_id("logo_link")
print(logo.get_attribute("style"))

