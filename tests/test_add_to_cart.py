from pages.login_page import LoginPage # type: ignore
from pages.inventory_page import InventoryPage # type: ignore


def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Abrir site + login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Validar que está na página Products
    assert inventory_page.get_title() == "Products"

    # Adicionar produto
    inventory_page.add_backpack_to_cart()

    # Validar carrinho com 1 item
    assert inventory_page.get_cart_count() == "1"
