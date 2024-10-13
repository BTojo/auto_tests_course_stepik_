from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открываем браузер и переходим на страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля: имя, фамилия, email

    firstname_name = browser.find_element(By.NAME, "firstname")
    firstname_name.send_keys("Aaa")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Bbb")

    email_name = browser.find_element(By.NAME, "email")
    email_name.send_keys("Ccc")


    # Определяем путь к текущей директории и создаем путь к файлу
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")


    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Ждем, чтобы успеть скопировать результат
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()