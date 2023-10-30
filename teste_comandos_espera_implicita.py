from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(15)

browser.maximize_window()
browser.get("https://chercher.tech/practice/implicit-wait-example")

checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
assert checkbox.is_displayed()
time.sleep(3)
print("O Checkbox está na tela")

