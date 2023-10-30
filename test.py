from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")
time.sleep(1)

# find_element()
# username = browser.find_element(By.ID, "user-name")
# password = browser.find_element(By.ID, "password")

# username.send_keys("standard_user")
# password.send_keys("secret_sauce")

# time.sleep(2)

# browser.quit()

# find_elements()
auth_fields = browser.find_elements(By.XPATH, '//*[@class = "input_error form_input"]')
print(auth_fields)
print(len(auth_fields))
assert len(auth_fields) == 2, "o tamanho do número de elementos encontrados é diferente do esperado"