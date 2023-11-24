from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")
time.sleep(1)

# .find_element()
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
bnt_login = browser.find_element(By.ID, "login-button")

# .send_keys()
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# .click()
bnt_login.click()
time.sleep(2)

# .text()
product_title = browser.find_element(By.XPATH, "//span[@class='title']")
print(product_title.text)
assert product_title.text == "Products"

# .get_attribute()
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print(img_backpack.get_attribute("alt"))

browser.quit()