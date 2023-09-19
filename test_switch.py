from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)
elem = driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(2)
elem = driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
