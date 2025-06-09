
#test_loginPage.py
import os
import json
import pytest
from SauceDemo_PYtest.Pages.login_page import LoginPage

# Load JSON once at module level
current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, '..', 'Pages', 'test_data', 'login_test_data.json')

with open(os.path.abspath(json_path), 'r') as f:
    test_data = json.load(f)

@pytest.mark.login  # <-- add this marker
@pytest.mark.parametrize("case", test_data)
def test_login_cases(init_driver, case):
    login_page = LoginPage(init_driver)

    username = case['username']
    password = case['password']
    expected_result = case['expected_result']

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    if expected_result == "success":
        assert login_page.is_dashboard_displayed(), "Dashboard should be displayed for valid login."
    else:
        error = login_page.get_error_message()
        if expected_result == "invalid_credentials":
            assert error == "Epic sadface: Username and password do not match any user in this service"
        elif expected_result == "empty_fields":
            assert error == "Epic sadface: Username is required"
        elif expected_result == "missing_password":
            assert error == "Epic sadface: Password is required"
        elif expected_result == "missing_username":
            assert error == "Epic sadface: Username is required"
