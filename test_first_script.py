from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")
time.sleep(2)

browser.find_element(By.LINK_TEXT, "user-name").click()
time.sleep(3)