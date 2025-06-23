from selenium import webdriver
import time

driver=webdriver.Edge()

url="https://www.saucedemo.com"
driver.get(url)
driver.maximize_window()
time.sleep(3)

driver.quit()
