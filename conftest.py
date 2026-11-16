import json
import os
from pathlib import Path

import pytest


@pytest.fixture(scope="session", autouse=True)
def use_data_test_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(scope="session")
def users():
    path = Path(__file__).parent / "test_data" / "users.json"
    with open(path) as file:
        return json.load(file)


@pytest.fixture(scope="session")
def password():
    value = os.environ.get("SAUCE_PASSWORD")
    if not value:
        pytest.fail("Set the SAUCE_PASSWORD environment variable before running the tests.")
    return value