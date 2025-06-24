from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, timeout=30)
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

def is_login_successful(driver):
    wait = WebDriverWait(driver, timeout=30)
    return wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='oxd-main-menu']/li[8]/a")))

def is_login_failed(driver):
    wait = WebDriverWait(driver, timeout=30)
    return wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[1]/div/span")))
