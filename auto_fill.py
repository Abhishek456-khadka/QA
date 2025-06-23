from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import string
import random


driver = webdriver.Edge()  # You can also use Edge() for Microsoft Edge

# Open a website
url = "https://www.mindrisers.com.np/contact-us"  
driver.get(url)
driver.maximize_window()  # Maximize the browser window
driver.execute_script("window.scrollBy(0, 600);")  # Scroll down by 1000 pixels
time.sleep(2) # Wait for the page to load

email_field = driver.find_element(*(By.XPATH,'//input[@placeholder="Email"]'))
name_field = driver.find_element(*(By.XPATH,'//input[@placeholder="Name"]'))
phone_field = driver.find_element(*(By.XPATH,'//input[@placeholder="Phone"]'))
subject_field = driver.find_element(*(By.XPATH,'//*[@id="__next"]/div[1]/div[2]/section[1]/div/form/div[3]/div[4]/input'))
queries_field = driver.find_element(*(By.XPATH,'//*[@id="__next"]/div[1]/div[2]/section[1]/div/form/div[3]/div[5]/textarea'))


def generate_email(): #For Genrating random email
    domain = "abc.com"
    email_length = 5  
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

def generate_name(): #For Genrating random name
    return ''.join(random.choices(string.ascii_letters, k=8))

def generate_phone_number(): #For Genrating random phone number
    return "+977-98" + ''.join(random.choices(string.digits, k=8))

def generate_subject(): #For Genrating random name
    return ''.join(random.choices(string.ascii_letters, k=8))

def generate_queries(): #For Genrating random name
     sentence = ' '.join(  [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8))) for _ in range(15)]) + '.'
     return sentence.capitalize()


name = generate_name()
name_field.clear()
name_field.send_keys(name)
time.sleep(2)

email = generate_email() 
email_field.clear()
email_field.send_keys(email) # Generate a random email
time.sleep(2)

phone = generate_phone_number()
phone_field.clear()
phone_field.send_keys(phone)
time.sleep(2)

subject = generate_subject()
subject_field.clear()
subject_field.send_keys(subject)
time.sleep(2)

queries = generate_queries()
queries_field.clear()
queries_field.send_keys(queries)
time.sleep(2)

driver.quit()
