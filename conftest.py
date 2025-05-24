# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
