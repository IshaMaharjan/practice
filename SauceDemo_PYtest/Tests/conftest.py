

#conftest.py
from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def init_driver():
    print("-------setup--------")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver  #after all test cases
    print("-------teardown--------")
    driver.quit()

#test module is a Python file that contains test functions or test classes. For example, a file named test_math.py



@pytest.fixture
def login_page(init_driver):
    return LoginPage(init_driver)

@pytest.fixture
def product_page(init_driver):
    return ProductPage(init_driver)

@pytest.fixture
def cart_page(init_driver):
    return CartPage(init_driver)
