from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pytest

edge_path = r'C:\Users\DELL\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

@pytest.fixture(scope="module")
def driver():
    options = Options()
    services = Service(executable_path=edge_path)
    driver = webdriver.Chrome(options=options, service=services)
    yield driver
    driver.quit()
