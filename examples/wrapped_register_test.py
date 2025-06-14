import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from uuid import uuid4
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("https://isqm.kalhorn.org/src/register/register.html")

        driver.find_element(
            By.ID,
            "name"
        ).send_keys("Paul")
        driver.find_element(
            By.ID,
            "email"
        ).send_keys(f"{uuid4()}@gmail.com")
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
        self.assertEqual(actual_message, "Registration successful!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
