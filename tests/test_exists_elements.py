from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    """Проверка элементов на главной странице"""
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logo"]/a/img')))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="narbar-menu"]/ul/li[6]')))
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[1]')))
    WebDriverWait(browser, 1).until_not(EC.visibility_of_element_located((By.XPATH, '//*[@id="test"]')))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]/input')))


def test_catalog(browser):
    """Проверка элементов в каталоге"""
    browser.get(browser.current_url + 'index.php?route=product/category&language=en-gb&path=25_28')
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logo"]')))
    test_check_url = browser.current_url
    if test_check_url != 'http://192.168.31.84:8081/index.php?route=product/category&language=en-gb&path=25_28':
        raise ValueError(f'Тест находится на другой странице: {test_check_url}')
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-cart"]/div/button')))
    WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="product-list"]/div[2]/div/div[2]/div/h4')))
    WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="product-list"]/div[2]/div/div[1]/a/img')))
    WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="product-list"]/div[2]/div/div[1]/a/img')))


def test_goods_cart(browser):
    """Проверка элементов на странице карточки товара"""
    browser.get(browser.current_url + 'index.php?route=product/product&language=en-gb&product_id=49&path=57')
    test_check_url = browser.current_url
    if test_check_url != ('http://192.168.31.84:8081/index.php?route=product/product&language=en-gb&product_id=49&path'
                          '=57'):
        raise ValueError(f'Тест находится на другой странице: {test_check_url}')
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="header-cart"]/div/button')))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="button-cart"]')))
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[2]/a')))
    WebDriverWait(browser, 1).until_not(EC.visibility_of_element_located((By.XPATH, '//*[@id="test"]/input[3]')))
    WebDriverWait(browser, 1).until_not(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="column-left"]/div[1]/a[4]')))


def test_admin_page(browser):
    """Проверка элементов на странице логина"""
    browser.get(browser.current_url + 'administration/')
    test_check_url = browser.current_url
    if test_check_url != 'http://192.168.31.84:8081/administration/':
        raise ValueError(f'Тест находится на другой странице: {test_check_url}')

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header"]/div/a')))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-username"]')))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-password"]')))
    WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="form-login"]/div[3]/button')))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="footer"]')))


def test_register_user(browser):
    """Проверка элементов на странице регистрации пользователя"""
    browser.get(browser.current_url + 'index.php?route=account/register')
    test_check_url = browser.current_url
    if test_check_url != 'http://192.168.31.84:8081/index.php?route=account/register':
        raise ValueError(f'Тест находится на другой странице: {test_check_url}')

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input-firstname"]')))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input-password"]')))
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="account-register"]/ul/li[3]/a')))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logo"]')))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-newsletter"]')))
