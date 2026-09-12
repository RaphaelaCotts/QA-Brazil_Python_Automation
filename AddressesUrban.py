from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://cnt-2ec4dbdb-55d3-4c1d-aed2-17b8cb430e1a.containerhub.tripleten-services.com/")
time.sleep(2)

driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")
time.sleep(1)
driver.find_element(By.ID, "to").send_keys("1300 1st St")
time.sleep(1)
driver.quit()
