from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.page_title = (By.CLASS_NAME, "title")
        self.add_backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.page_title)
        ).text

    def add_backpack_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_backpack_button)
        ).click()

    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.cart_badge)
        ).text

    def open_cart(self):
        cart_icon = (By.CLASS_NAME, "shopping_cart_link")

        self.wait.until(
            EC.element_to_be_clickable(cart_icon)
        ).click()
