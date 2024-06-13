import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture(scope="module")
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file_path = os.path.join(current_dir, "index.html")
    driver.get(f"file:///{html_file_path}")

    yield driver
    driver.quit()

def test_title(browser):
    assert browser.title == "Página pruebav2"

if __name__ == '__main__':
    pytest.main()
