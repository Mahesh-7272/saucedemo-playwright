import json
import os
from pathlib import Path

import pytest


@pytest.fixture(scope="session", autouse=True)
def use_data_test_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


def load_test_data(file_name):
    path = Path(__file__).parent / "test_data" / file_name
    with open(path) as file:
        return json.load(file)


@pytest.fixture(scope="session")
def users():
    return load_test_data("users.json")


@pytest.fixture(scope="session")
def customer():
    return load_test_data("customer.json")


@pytest.fixture(scope="session")
def password():
    value = os.environ.get("SAUCE_PASSWORD")
    if not value:
        pytest.fail("Set the SAUCE_PASSWORD environment variable before running the tests.")
    return value