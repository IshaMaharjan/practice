#Product_page.py
from selenium.webdriver.common.by import By
from SauceDemo_PYtest.Pages.base_page import BasePage  # adjust import based on your structure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ProductPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")

    EXPECTED_URL = "https://www.saucedemo.com/inventory.html"

    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn_inventory.btn_primary.btn_small")

    REMOVE_BUTTON = (By.XPATH, "(//button[text()='Remove'])")

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        super().__init__(driver)

    def is_on_correct_page(self):
        return self.driver.current_url == self.EXPECTED_URL

    def is_title_correct(self):
        return self.validate_text(self.TITLE, "Products")

    def count_inventory_items(self):
        elements = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(elements)

    #------------------- cart, button functionality ----------------------
    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def is_remove_button_displayed(self):
        return self.is_element_visible(self.REMOVE_BUTTON)

    def add_all_items_to_cart(self):
        print("Adding all items to cart...")
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.btn_inventory')
        for i, button in enumerate(buttons):
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
                button.click()
                print(f"Clicked 'Add to Cart' button {i + 1}")
            except Exception as e:
                print(f"Failed to click 'Add to Cart' button {i + 1}: {e}")

    # to count the span number or number notification in cart
    def get_cart_count(self):
        if self.verify_element_present(self.CART_BADGE):
            return int(self.driver.find_element(*self.CART_BADGE).text)
        return 0

    #for filter feature in product page
    def select_sort_option(self, option_text):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        Select(dropdown).select_by_visible_text(option_text)

    def get_product_names(self):
        # Wait for product name elements to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]
