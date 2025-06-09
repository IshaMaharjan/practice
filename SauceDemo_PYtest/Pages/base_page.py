
#base_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def verify_element_present(self, locator):
        """Checks if an element is present in the DOM (not necessarily visible)."""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def is_element_visible(self, locator):
        """Checks if an element is visible on the page."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def validate_text(self, locator, expected_text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actual_text = element.text.strip()

        if not actual_text:  # If element.text is empty, try checking the 'value' attribute
            actual_text = element.get_attribute("value").strip()

        return actual_text == expected_text

    def get_element_attribute(self, locator, attribute_name):   #for Placeholder
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute_name)
    #
    # def get_number_of_elements(self, locator):
    #     elements = self.wait.until(EC.presence_of_all_elements_located(locator))
    #     return len(elements)

    def logout(self):
        """Logs out of the application."""
        try:
            # Try using your provided XPath
            menu_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Open Menu')]"))
            )
        except TimeoutException:
            # Fallback to actual working ID if XPath fails
            menu_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
            )
        menu_button.click()

        logout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))
        )
        logout_button.click()

    def slow_type(self, locator, text, delay=0.2):
        """Types text character by character with delay (for observation/demo)."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        for char in text:
            element.send_keys(char)
            time.sleep(delay)