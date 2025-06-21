
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


    def __init__(self, driver):
        super().__init__(driver)

    def enterFirstName(self, firstName):
        self.send_keys(self.FirstName, firstName)

    def enterLastName(self, lastName):
        self.LastName = lastName

    def enterZipCode(self, zipCode):
        self.ZipCode = zipCode

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

