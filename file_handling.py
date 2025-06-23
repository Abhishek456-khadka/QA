from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Edge()  # You can also use Edge() for Microsoft Edge

# Open a website
url = "https://formy-project.herokuapp.com/form.com"
driver.get(url)
driver.maximize_window()  # Maximize the browser window
time.sleep(2) # Wait for the page to load

first_name_field = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name_field.send_keys("John")  # Enter first name
time.sleep(2)

last_name_field = driver.find_element(By.XPATH, "//input[@id='last-name']")  # Locate the last name field
last_name_field.send_keys("Doe")  # Enter last name
time.sleep(2)

Job_title_field = driver.find_element(By.XPATH,"//input[@id='job-title']")  # Locate the job title field
Job_title_field.send_keys("QA Engineer")  # Enter job title
time.sleep(2)

education_field = driver.find_element(By.XPATH,'//*[@id="radio-button-1"]')  # Locate the education field
education_field.click()  # Click on the education option
time.sleep(2)

gender_field1 = driver.find_element(By.XPATH,'//*[@id="checkbox-1"]')  # Locate the gender field
gender_field1.click()  # Click on the gender option
gender_field2 = driver.find_element(By.XPATH,'//*[@id="checkbox-2"]')  # Locate other option
gender_field2.click()  # Click on the other option
time.sleep(2)

driver.execute_script("window.scrollBy(0,1000);")
time.sleep(2)  # Scroll down by 1000 pixels

years_field = driver.find_element(By.XPATH,'//*[@id="select-menu"]')  # Locate the years of experience field
years_field.click()  

select_years = driver.find_element(By.XPATH,'//*[@id="select-menu"]/option[2]')  # Select the option for 2 years
select_years.click()  # Click on the option
time.sleep(2)

date_field = driver.find_element(By.XPATH,'//*[@id="datepicker"]')  # Locate the date field
date_field.send_keys("01/01/2023")  # Enter a date
time.sleep(2)

submit_button = driver.find_element(By.XPATH,'/html/body/div/form/div/div[8]/a')  # Locate the submit button
submit_button.click()  # Click on the submit button

time.sleep(2)  # Wait for the form submission to complete
driver.quit()