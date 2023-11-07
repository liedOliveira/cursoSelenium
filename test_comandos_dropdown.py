import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

# select_by_visible_text()
dropdown_products = Select(browser.find_element(By.XPATH, "//*[@id='first' and @class='col-lg-3']"))
dropdown_products.select_by_visible_text("Google")
time.sleep(2)

# select_by_value()
dropdown_animals = Select(browser.find_element(By.XPATH, "//*[@id='animals' and @class='col-lg-3']"))
dropdown_animals.select_by_value("big baby cat")
time.sleep(2)
dropdown_animals.select_by_index(1)

dropdown_food = Select(browser.find_element(By.XPATH, "//select[@id='second']"))
dropdown_food.select_by_visible_text("Pizza")
dropdown_food.select_by_visible_text("Donut")
dropdown_food.select_by_visible_text("Burger")
time.sleep(3)

