from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization_logout(browser):
    """Вход и выход в админку с проверкой"""
    browser.get(browser.current_url + 'administration/')
    test_check_url = browser.current_url
    if test_check_url != 'http://192.168.31.84:8081/administration/':
        raise ValueError(f'Адреса не равны: {test_check_url}')
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="input-username"]'))).send_keys('user')
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="input-password"]'))).send_keys('bitnami')
    WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="form-login"]/div[3]/button'))).click()
    WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-profile"]/a'))).click()
    WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-logout"]'))).click()
    test_check_url = browser.current_url
    if test_check_url != 'http://192.168.31.84:8081/administration/index.php?route=common/login':
        raise ValueError(f'Тест находится на другой странице: {test_check_url}')


