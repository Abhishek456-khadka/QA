import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://google.com")
googleSearchBox= driver.find_element(By.ID, "APjFqb")
googleSearchBox.send_keys("Automation")
import time

time.sleep(2)  # crude wait, better use explicit wait

buttons = driver.find_elements(By.NAME, "btnK")
for btn in buttons:
    if btn.is_displayed() and btn.is_enabled():
        btn.click()
        break
time.sleep(2)
driver.quit()