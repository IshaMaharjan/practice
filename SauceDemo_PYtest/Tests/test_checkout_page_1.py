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
