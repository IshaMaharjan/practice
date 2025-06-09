
#cart_page.py
from SauceDemo_PYtest.Pages.base_page import BasePage
from selenium.webdriver.common.by import By



class CartPage(BasePage):
    CART_PAGE_TITLE = (By.CSS_SELECTOR, "span.title[data-test='title']")
    CART_EXPECTED_URL = "https://www.saucedemo.com/cart.html"
    CART_ICON_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-backpack']")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    EXPECTED_INVENTORY_PAGE ="https://www.saucedemo.com/inventory.html"
    EXPECTED_CHECKOUT_PAGE = "https://www.saucedemo.com/checkout-step-one.html"



    def __init__(self, driver):
        super().__init__(driver)

    def is_on_correct_page(self):
        return self.driver.current_url == self.CART_EXPECTED_URL

    def is_title_correct(self):
        return self.validate_text(self. CART_PAGE_TITLE, "Your Cart")

    def count_cart_items(self):
        elements = self.driver.find_elements(*self. CART_ITEM)
        return len(elements)

    def click_remove_button(self):
        remove_button = self.driver.find_element(*self.REMOVE_BUTTON)
        if remove_button:
            remove_button.click()
        else:
            raise Exception("No remove button found on cart page")

    def click_cart_icon(self):
        self.click(self.CART_ICON_BUTTON)

    def click_continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
