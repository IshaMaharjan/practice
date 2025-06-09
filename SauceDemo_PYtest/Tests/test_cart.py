#test_cart.py
import time
import pytest
from SauceDemo_PYtest.Pages.login_page import LoginPage
from SauceDemo_PYtest.Pages.Product_page import ProductPage
from SauceDemo_PYtest.Pages.cart_page import CartPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# To validate URL and page title
@pytest.mark.usefixtures("init_driver")
def test_validate_cart_page(init_driver):
    login_page = LoginPage(init_driver)
    login_page.login()

    # ESCAPE to dismiss the popup
    ActionChains(init_driver).send_keys(Keys.ESCAPE).perform()

    #cart icon is clicked
    init_driver.find_element(*CartPage.CART_ICON_BUTTON).click()

    cart_page = CartPage(init_driver)
    assert cart_page.is_on_correct_page(), "URL mismatch after login"
    assert cart_page.is_title_correct(), "Title is incorrect"

    time.sleep(5)

@pytest.mark.usefixtures("init_driver")
def test_remove_item_from_cart(init_driver):
    login_page = LoginPage(init_driver)
    login_page.login()

    ActionChains(init_driver).send_keys(Keys.ESCAPE).perform()

    # Add all items
    product_page = ProductPage(init_driver)
    product_page.add_all_items_to_cart()

    # Go to cart
    cart_page = CartPage(init_driver)
    cart_page.click_cart_icon()

    # Check initial count
    initial_count = cart_page.count_cart_items()
    assert initial_count > 0, "Cart is unexpectedly empty"

    # Click remove button on one item
    cart_page.click_remove_button()  # <-- You need this method to click one remove button

    # Get new count after removal
    new_count = cart_page.count_cart_items()

    # Assert the count decreased by 1
    assert new_count == initial_count - 1, f"Expected {initial_count - 1} items after removal, but found {new_count}"

    time.sleep(5)


@pytest.mark.usefixtures("init_driver")
def test_continue_shopping_button(init_driver):
    login_page = LoginPage(init_driver)
    login_page.login()

    cart_page = CartPage(init_driver)
    cart_page.click_cart_icon()  # Go to cart page

    cart_page.click_continue_shopping()

    # Use the variable from the CartPage class like this:
    assert init_driver.current_url == cart_page.EXPECTED_INVENTORY_PAGE, "Continue Shopping button did not navigate correctly"



@pytest.mark.usefixtures("init_driver")
def test_checkout_button(init_driver):
    login_page = LoginPage(init_driver)
    login_page.login()

    cart_page = CartPage(init_driver)
    cart_page.click_cart_icon()  # Navigate to cart page

    cart_page.click_checkout()  # Click checkout button

    assert init_driver.current_url == cart_page.EXPECTED_CHECKOUT_PAGE, "Checkout button did not navigate correctly"
