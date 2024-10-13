from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем браузер и переходим на страницу
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)




    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Ждем, чтобы успеть скопировать результат
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()