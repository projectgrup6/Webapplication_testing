from pages.login_page import login, is_login_successful, is_login_failed

def test_login_pass(driver):
    login(driver, "Admin", "admin123")
    assert is_login_successful(driver).is_displayed()
    print("Login Passed")

def test_login_failed(driver):
    login(driver, "Admin", "admin23")
    assert is_login_failed(driver).is_displayed()
    print("Login Failed")
