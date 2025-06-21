
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from SauceDemo_PYtest.Pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
import pytest
from SauceDemo_PYtest.Pages.login_page import LoginPage
from SauceDemo_PYtest.Pages.Product_page import ProductPage
from SauceDemo_PYtest.Pages.cart_page import CartPage



class CheckoutPage1(BasePage):
    FirstName = (By.XPATH, "//input[@id='first-name']")
    LastName = (By.XPATH, "//input[@id='last-name']")
    ZipCode = (By.XPATH, "//input[@id='postal-code']")
    Continue =(By.ID, "continue")
    Cancel = (By.ID, "cancel")
    Checkout_title = (By.CSS_SELECTOR, "[data-test='title']")
    Checkout_URL = "https://www.saucedemo.com/checkout-step-one.html"
    Error_Message = (By.CSS_SELECTOR, "h3[data-test='error']")



    def __init__(self, driver):
        super().__init__(driver)

    def enterFirstName(self, firstName):
        self.send_keys(self.FirstName, first_name)

    def enterLastName(self, lastName):
        self.send_keys(self.LastName, last_name)
    def enterZipCode(self, zipCode):
        self.send_keys(self.ZipCode, zip_code)

    def clickCancel(self):
        self.click(self.Cancel)

    def clickContinue(self):
        self.click(self.Continue)

    def getto_checkout_page(self):
        login_page = LoginPage(self.driver)
        login_page.login()

        cart_page = CartPage(self.driver)
        cart_page.click_cart_icon()

        cart_page.click_checkout()

        checkout_page = CheckoutPage1(self.driver)

        assert self.driver.current_url == self.Checkout_URL
        assert self.driver.title == self.Checkout_title

    def wait_for_checkout_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.FirstName))
        except TimeoutException:
            raise AssertionError("checkout page did not load in time — firstname field not found.")

    def is_bil_displayed(self):
        try:
            Title = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "title")) #swag Lab
            )
            return Title.is_displayed()
        except TimeoutException:
            return False

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.Error_Message)).text