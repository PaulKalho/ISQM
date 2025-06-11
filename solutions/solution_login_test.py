import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExerciseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver

        driver.get("https://isqm.kalhorn.org/")

        driver.find_element(By.ID, "email").send_keys("kalhornpaul@gmail.com")
        driver.find_element(By.ID, "password").send_keys("Test&123")

        driver.find_element(By.TAG_NAME, "button").click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://isqm.kalhorn.org/src/shop/shop.html")
        )

        self.assertEqual(driver.title, "Shop Page")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
