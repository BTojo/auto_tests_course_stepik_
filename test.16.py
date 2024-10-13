from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной


try:
    # Открываем браузер и переходим на страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))

    book_button = browser.find_element(By.CSS_SELECTOR, "#book")
    book_button.click()


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)




    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit_button.click()

finally:
    # Ждем, чтобы успеть скопировать результат
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()


