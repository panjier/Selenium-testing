from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
time.sleep(2)

driver.find_element(By.ID, "alertButton").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
