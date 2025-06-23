from selenium import webdriver
import time

driver = webdriver.Edge()
url="https://triphimalaya.com"

driver.get(url)
driver.maximize_window()

time.sleep(4)
driver.quit()