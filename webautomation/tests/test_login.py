from pages.login_page import login, is_login_successful, is_login_failed

def test_login_pass(driver):
    login(driver, "Admin", "admin123")
    assert is_login_successful(driver).is_displayed()
    print("Login Passed")

def is_login_failed(driver):
    wait = WebDriverWait(driver, timeout=20)
    try:
        return wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Invalid credentials')]"))
        )
    except Exception as e:
        print("❌ Could not find login error message.")
        driver.save_screenshot("login_failed_debug.png")
        raise e
