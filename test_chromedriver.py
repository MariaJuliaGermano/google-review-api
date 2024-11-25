from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com")

sleep(80)

driver.quit()