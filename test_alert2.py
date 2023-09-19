from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

driver.find_element(By.ID, "confirmexample").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
