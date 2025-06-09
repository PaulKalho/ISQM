import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExerciseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def login(self, mail, password):
        driver = self.driver

        driver.get("https://isqm.kalhorn.org/")

        driver.find_element(By.ID, "email").send_keys(mail)
        driver.find_element(By.ID, "password").send_keys(password)

        driver.find_element(By.TAG_NAME, "button").click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://isqm.kalhorn.org/src/shop/shop.html")
        )

    def test_register(self):
        driver = self.driver
        driver.get("https://isqm.kalhorn.org/src/register/register.html")

        driver.find_element(By.ID, "name").send_keys("tester")
        driver.find_element(By.ID, "email").send_keys("tester@mail.de")
        driver.find_element(By.ID, "street").send_keys("Eupener Str")
        driver.find_element(By.ID, "housenr").send_keys("70")
        driver.find_element(By.ID, "postcode").send_keys("52066")
        driver.find_element(By.ID, "city").send_keys("Aachen")
        driver.find_element(By.ID, "country").send_keys("Germany")
        driver.find_element(By.ID, "password").send_keys("test")

        driver.find_element(By.TAG_NAME, "button").click()

        _ = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"), "Registration successful!")
        )

        # Now get the actual text and assert it
        actual_message = driver.find_element(By.ID, "message").text
        self.assertEqual(actual_message, "Registration successful!")

    def test_order(self):
        self.login("tester@mail.de", "test")

        driver = self.driver

        # Wait for the page to load
        driver.implicitly_wait(3)

        product_cards = self.driver.find_elements(
            By.CLASS_NAME, "product-card")

        second_product_button = product_cards[1].find_element(
            By.TAG_NAME, "button")
        second_product_button.click()

        # Wait
        driver.implicitly_wait(3)

        cart_button = driver.find_element(By.ID, "cartButton")
        self.assertEqual(cart_button.text.strip(), "Cart (1)")

        cart_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://isqm.kalhorn.org/src/cart/cart.html")
        )

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Wait
        driver.implicitly_wait(5)

        cart_items = self.driver.find_element(By.ID, "cartItems")
        children = cart_items.find_elements(
            By.XPATH, "./*")  # finds all direct children
        self.assertEqual(len(children), 0,
                         "Cart should be empty but it has items.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
