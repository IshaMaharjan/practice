#login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from SauceDemo_PYtest.Pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
class LoginPage(BasePage):
    USERNAME = (By.XPATH, "//input[@name='user-name']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.TAG_NAME, "h3")
    DASHBOARD_DISPLAY = (By.XPATH, "//div[@class='app_logo']")
    # LOGIN_LOGO = (By.CLASS_NAME, "login_logo")

    def __init__(self, driver):
        super().__init__(driver)
    def enter_username(self, username):
        self.type(self.USERNAME, username)
    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text

    def is_dashboard_displayed(self):
        return self.wait.until(EC.presence_of_element_located(self.DASHBOARD_DISPLAY)).is_displayed()

    def get_username_placeholder(self):
        return self.get_element_attribute(self.USERNAME, "placeholder")


    def get_password_placeholder(self):
        return self.get_element_attribute(self.PASSWORD, "placeholder")



    def get_login_button_text(self):
        return self.driver.find_element(*self.LOGIN_BUTTON).get_attribute("value")

    def is_login_page_displayed(self):
        """Verifies that the login page is displayed by checking for login logo."""
        try:
            logo = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")) #swag Lab
            )
            return logo.is_displayed()
        except TimeoutException:
            return False

    def login(self, username="standard_user", password="secret_sauce"):
        self.slow_type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
