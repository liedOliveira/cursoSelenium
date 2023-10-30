from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com/")
time.sleep(1)

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

# is.displayed()
print(username.is_displayed())
assert username.is_displayed(), "O elemento não está sendo exibido na tela"

# is.enabled()
username.is_enabled()
print(username.is_enabled())
assert username.is_enabled(), "O elemento não está habilitado"

# is.selected()
print(checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()
time.sleep(2)
checkbox_remember_me.click()

print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()