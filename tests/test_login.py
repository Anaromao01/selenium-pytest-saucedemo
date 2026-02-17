from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from pages.login_page import LoginPage # type: ignore
from pages.inventory_page import InventoryPage # type: ignore



def test_login_success(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password = driver.find_element(By.ID, "password")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert title.text == "Products"


