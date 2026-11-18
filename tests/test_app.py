
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )

    yield driver
    driver.quit()


def test_homepage(browser):
    browser.get("http://web:5000")

    assert "Welcome to DevOps Lab" in browser.page_source


def test_addition(browser):
    browser.get("http://web:5000/add?a=10&b=20")

    result = browser.find_element(By.ID, "result").text

    assert result == "Result: 30"
