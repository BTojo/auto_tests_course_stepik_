from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")  # Замените value1 на "input", чтобы найти первое поле
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")  # Замените value2 на "last_name"
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")  # Замените value3 на "form-control"
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

# option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
# option1.click()

#<input class="check-input" type="checkbox" id="robotCheckbox" required="">
#input.check-input[type="checkbox"]

# browser.find_element(By.TAG_NAME, "select").click()               -->  поиск списка и его раскрытие
# browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()  или browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

Есть более удобный способ, для которого используется специальный класс Select из библиотеки WebDriver. Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select. Далее можно найти любой вариант из списка с помощью метода select_by_value(value):

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index). Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python", нужно использовать select.select_by_index(1), так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".