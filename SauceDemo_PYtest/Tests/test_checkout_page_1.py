import os
import json
import pytest
from SauceDemo_PYtest.Pages.CheckoutPage1 import CheckoutPage1

# Load test data
current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, '..', 'Pages', 'test_data', 'checkout_data.json')

try:
    with open(os.path.abspath(json_path), 'r') as f:
        test_data = json.load(f)
except Exception as e:
    print(f"Failed to load test data: {e}")
    test_data = []

@pytest.mark.login
@pytest.mark.parametrize("case", test_data)
def test_checkout_different_inputs(init_driver, case):
    checkout_page = CheckoutPage1(init_driver)
    checkout_page.getto_checkout_page()  # We are now at the checkout form page

    # Get test inputs
    first_name = case.get("first_name", "")
    last_name = case.get("last_name", "")  # ✅ Corrected key name: was 'lastname'
    zip_code = case.get("zip_code", "")
    expected_result = case.get("expected_result", "")

    # Fill the form
    checkout_page.wait_for_checkout_page()
    checkout_page.enterFirstName(first_name)  # ✅ Pass the actual value
    checkout_page.enterLastName(last_name)
    checkout_page.enterZipCode(zip_code)
    checkout_page.clickContinue()

    # Assert based on expected result
    if expected_result == "success":
        assert checkout_page.is_bil_displayed(), "Expected bill not visible"
    else:
        error = checkout_page.get_error_message()
        if expected_result == "missing_first_name":
            assert error == "Error: First Name is required"
        elif expected_result == "missing_last_name":
            assert error == "Error: Last Name is required"
        elif expected_result == "empty_zip":
            assert error == "Error: Postal Code is required"
