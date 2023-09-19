from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

driver.find_element(By.ID, "promtButton").click()
time.sleep(2)
driver.switch_to.alert.send_keys("Panji Erlangga")
time.sleep(2)
driver.switch_to.alert.accept()
