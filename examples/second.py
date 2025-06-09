from selenium import webdriver
from selenium.webdriver.common.by import By

from uuid import uuid4

import time

driver = webdriver.Firefox()

driver.get("https://isqm.kalhorn.org/src/register/register.html")

name = driver.find_element(
    By.ID,
    "name"
)
email_input = driver.find_element(
    By.ID,
    "email"
)
street_input = driver.find_element(
    By.ID,
    "street"
)
housenr_input = driver.find_element(
    By.ID,
    "housenr"
)
postcode_input = driver.find_element(
    By.ID,
    "postcode"
)
city_input = driver.find_element(
    By.ID,
    "city"
)
country_input = driver.find_element(
    By.ID,
    "country"
)
password_input = driver.find_element(
    By.ID,
    "password"
)
submit_button = driver.find_element(
    By.TAG_NAME,
    "button"
)

name.send_keys("Paul")
time.sleep(1)
email_input.send_keys(f"{uuid4()}@gmail.com")
time.sleep(1)
street_input.send_keys("Eupener Str.")
time.sleep(1)
housenr_input.send_keys("70")
time.sleep(1)
postcode_input.send_keys("52066")
time.sleep(1)
city_input.send_keys("Aachen")
time.sleep(1)
country_input.send_keys("Germany")
time.sleep(1)
password_input.send_keys("Test&123")
time.sleep(1)

submit_button.click()

time.sleep(5)

driver.quit()
