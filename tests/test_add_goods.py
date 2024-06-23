import time
from selenium.webdriver.common.by import By


def test_add_goods(browser):
    """проверка добавления твоара в корзину"""
    span_elem = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    if span_elem.text != '0 item(s) - $0.00':
        raise ValueError(f'В начале теста крзина не пуста: {span_elem.text}')
    elem = browser.find_element(By.XPATH,
                                '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')
    browser.execute_script("arguments[0].scrollIntoView(true);", elem)
    time.sleep(5)
    elem.click()
    elem = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    browser.execute_script("arguments[0].scrollIntoView(true);", elem)
    time.sleep(5)
    span_elem = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    if span_elem.text != '1 item(s) - $602.00':
        raise ValueError(f'Сумма в корзине не соответствует ожидаемой: {span_elem.text}')