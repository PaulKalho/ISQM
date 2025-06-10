from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    driver = webdriver.Firefox()
    driver.get("https://isqm.kalhorn.org/src/register/register.html")

    driver.find_element(
        By.ID,
        "name"
    ).send_keys("Paul")
    driver.find_element(
        By.ID,
        "email"
    ).send_keys("kalhornpaul@gmail.com")
    driver.find_element(
        By.ID,
        "street"
    ).send_keys("Eupener Str.")
    driver.find_element(
        By.ID,
        "housenr"
    ).send_keys("70")
    driver.find_element(
        By.ID,
        "postcode"
    ).send_keys("52066")
    driver.find_element(
        By.ID,
        "city"
    ).send_keys("Aachen")
    driver.find_element(
        By.ID,
        "country"
    ).send_keys("Germany")
    driver.find_element(
        By.ID,
        "password"
    ).send_keys("Test&123")
    driver.find_element(
        By.TAG_NAME,
        "button"
    ).click()

    _ = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, "message"), "Registration successful!")
    )
    actual_message = driver.find_element(By.ID, "message").text

    if actual_message != "Registration successful!":
        raise Exception("TEST FAILED")


if __name__ == "__main__":
    test_login()
