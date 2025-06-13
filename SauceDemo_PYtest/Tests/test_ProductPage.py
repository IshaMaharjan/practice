
#test_ProductPage.py
import json
import os

# Correct path to: SauceDemo_PYtest/Pages/test_data/test_data.json
data_path = os.path.join(
    os.path.dirname(__file__),
    '..',  # up from Tests to SauceDemo_PYtest
    'Pages',
    'test_data',
    'ProductPage_data.json'
)
data_path = os.path.abspath(data_path)

with open(data_path, 'r') as f:
    TEST_DATA = json.load(f)



from SauceDemo_PYtest.Pages.login_page import LoginPage
from SauceDemo_PYtest.Pages.Product_page import ProductPage
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.mark.usefixtures("init_driver")
class TestProductPage:

    # validates url of page, title, and counts numbers of products in inventory
    def test_validate_product_page(self,init_driver):
        login_page = LoginPage(init_driver)
        login_page.login()

        # ESCAPE to dismiss the popup
        ActionChains(init_driver).send_keys(Keys.ESCAPE).perform()

        product_page = ProductPage(init_driver)
        # Use JSON data
        assert product_page.is_on_correct_page(), "URL mismatch after login"
        assert product_page.is_title_correct(), "Product title is incorrect"

        item_count = product_page.count_inventory_items()
        expected_count = TEST_DATA["product_page"]["expected_item_count"]
        assert item_count == expected_count, f"Expected {expected_count} inventory items on the page"


    # to test after clicking "Add to cart" change into "Remove"
    def test_add_to_cart_functionality(self,init_driver):
        login_page = LoginPage(init_driver)
        login_page.login()

        # # ESCAPE to dismiss the popup
        ActionChains(init_driver).send_keys(Keys.ESCAPE).perform()

        product_page = ProductPage(init_driver)

        # Add the first item to the cart
        product_page.click_add_to_cart()

        # Verify the button changed to "Remove"
        assert product_page.is_remove_button_displayed(), "Remove button not displayed after adding to cart"

        # Verify the cart badge shows 1 item
        cart_count = product_page.get_cart_count()
        assert cart_count == 1, f"Expected cart count to be 1, but got {cart_count}"



    # To test adding all items to cart: observe button and cart count
    @pytest.mark.cart
    def test_add_all_items_to_cart(self,init_driver):
        login_page = LoginPage(init_driver)
        login_page.login()

        # Dismiss any popup by pressing ESCAPE
        ActionChains(init_driver).send_keys(Keys.ESCAPE).perform()

        product_page = ProductPage(init_driver)
        assert product_page.is_on_correct_page(), "Not on the product page"

        product_page.add_all_items_to_cart()

        cart_count = product_page.get_cart_count()
        assert cart_count == 6, f"Expected 6 items in cart, but found {cart_count}"

        # Verify that all buttons have changed to 'Remove'
        remove_buttons = init_driver.find_elements(By.XPATH, "//button[text()='Remove']")
        assert len(remove_buttons) == 6, f"Expected 6 'Remove' buttons, but found {len(remove_buttons)}"



    # to test the filter according to name of item in AC order
    @pytest.mark.filter
    def test_sort_by_name_a_to_z(self,init_driver):
        login_page = LoginPage(init_driver)
        login_page.login()

        # Dismiss any popup by pressing ESCAPE
        ActionChains(init_driver).send_keys(Keys.ESCAPE).perform()

        product_page = ProductPage(init_driver)
        product_page.select_sort_option("Name (A to Z)")
        names = product_page.get_product_names()
        assert names == sorted(names), "Products are not sorted A to Z"


    # to test the filter according to name of item in DSC order
    @pytest.mark.filter
    def test_sort_by_name_z_to_a(self, init_driver):
        login_page = LoginPage(init_driver)
        login_page.login()

        ActionChains(init_driver).send_keys(Keys.ESCAPE).perform()

        product_page = ProductPage(init_driver)
        product_page.select_sort_option("Name (Z to A)")
        names = product_page.get_product_names()
        assert names == sorted(names, reverse=True), "Products are not sorted Z to A"


    @pytest.mark.filter
    def test_sort_by_price_low_to_high(self,init_driver):
        login_page = LoginPage(init_driver)
        login_page.login()

        ActionChains(init_driver).send_keys(Keys.ESCAPE).perform()

        product_page = ProductPage(init_driver)
        product_page.select_sort_option("Price (low to high)")
        prices = product_page.get_product_prices()
        assert prices == sorted(prices), "Products are not sorted by price low to high"

    @pytest.mark.filter
    def test_sort_by_price_high_to_low(self,init_driver):
        login_page = LoginPage(init_driver)
        login_page.login()

        ActionChains(init_driver).send_keys(Keys.ESCAPE).perform()

        product_page = ProductPage(init_driver)
        product_page.select_sort_option("Price (high to low)")
        prices = product_page.get_product_prices()
        assert prices == sorted(prices, reverse=True), "Products are not sorted by price high to low"


