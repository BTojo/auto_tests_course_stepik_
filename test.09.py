import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    option2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    print(option1.text)
    print (option2.text)
    result = int(option1.text) + int(option2.text)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_visible_text(str(result))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
