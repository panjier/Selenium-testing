from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

driver.maximize_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
