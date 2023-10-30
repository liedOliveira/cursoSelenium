from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
wait = WebDriverWait(browser, 30)

# alert_is_present()
browser.find_element(By.ID, "alert").click()
wait.until(EC.alert_is_present())
time.sleep(3)

# text_to_be_present_in_element()
browser.find_element(By.ID, "populate-text").click()
wait.until(EC.text_to_be_present_in_element(locator=(By.CLASS_NAME, "target-text"), text_=("Selenium Webdriver")))
target_text = browser.find_element(By.CLASS_NAME, "target-text").text
assert target_text == "Selenium Webdriver", "O texto não está sendo exibido na tela"
time.sleep(3)

# element_to_be_clickable()
browser.find_element(By.XPATH, "//*[@id='display-other-button']").click()
wait.until(EC.element_to_be_clickable((By.ID, "hidden")))
hidden_bnt = browser.find_element(By.XPATH, "//*[@id='display-other-button']")
assert hidden_bnt.is_displayed(), "O botão não está visível"
time.sleep(2)

browser.find_element(By.XPATH, "//*[@id='enable-button']").click()
wait.until(EC.element_to_be_clickable((By.ID, "disable")))
disable_bnt = browser.find_element(By.XPATH, "//*[@id='enable-button']")
assert disable_bnt.is_enabled(), "O botão não está habilitado"
time.sleep(3)

# element_to_be_selected()
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")
browser.find_element(By.ID, "checkbox").click()
wait.until(EC.element_to_be_selected((checkbox)))
assert checkbox.is_selected(), "A checkbox não está selecionada"
time.sleep(3)
