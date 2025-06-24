from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import time
import pytest

edge_path = r'C:\Users\DELL\drivers\msedgedriver.exe'

@pytest.fixture(scope="module")
def driver():
    options = Options()
    services = Service(executable_path=edge_path)
    driver = webdriver.Edge(options=options, service=services)
    yield driver
    driver.quit()