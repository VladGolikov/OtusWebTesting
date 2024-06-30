from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_change_сurrency_сatalog(browser):
    # Открыть выбор валют
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/a'))).click()
    # Изменить на фунты стерлингоа
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a'))).click()
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/a'))).click()
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/div/a'))).click()
    element = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="product-list"]/div[3]/div/div[2]/div/div/span[1]')))
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    if element.text[0] != '£':
        raise ValueError(f'Цена не изменилась на фунты стерлингов: {element.text}')
    element = browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]')
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    if element.text[0] != '£':
        raise ValueError(f'Цена не изменилась на фунты стерлингов в корзине: {element.text}')


def test_change_currency_main(browser):
    # Открыть выбор валют
    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/a'))).click()
    # Изменить на евро
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a'))).click()
    element = browser.find_element(By.XPATH,
                                   '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    if element.text != '472.33€':
        raise ValueError(f'Цена не изменилась на евро: {element.text}')
    browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]').click()
    element = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    element = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    if element.text != '1 item(s) - 472.33€':
        raise ValueError(f'Цена не изменилась на евро в корзине: {element.text}')
