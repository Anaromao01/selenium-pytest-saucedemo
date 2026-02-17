from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_success(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Step 1 - Open login page
    login_page.open()

    # Step 2 - Perform login
    login_page.login("standard_user", "secret_sauce")

    # Step 3 - Validate inventory page title
    assert inventory_page.get_title() == "Products"
