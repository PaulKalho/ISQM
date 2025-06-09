from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.fh-aachen.de/")

driver.add_cookie({"name": "example_cookie", "value": "12345"})

driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

driver.back()

time.sleep(2)

driver.forward()

driver.refresh()

time.sleep(2)

driver.quit()
