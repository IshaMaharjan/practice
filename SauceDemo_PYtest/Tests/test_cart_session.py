import pytest

@pytest.mark.usefixtures("init_driver", "login_page", "product_page", "cart_page")
class TestCartFunctionality:

    def test_cart_persistence_after_reload(self, login_page, product_page, cart_page, init_driver):
        login_page.login("standard_user", "secret_sauce")

        product_page.add_to_cart("Sauce Labs Backpack")
        product_page.open_cart()
        assert cart_page.has_item("Sauce Labs Backpack"), "Item not found in cart before reload"

        init_driver.refresh()
        assert cart_page.has_item("Sauce Labs Backpack"), "Item not found in cart after reload"