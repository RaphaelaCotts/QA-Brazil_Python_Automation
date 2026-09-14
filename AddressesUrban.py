from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://cnt-01fba740-aab3-4ba6-ad81-5c68feaed5b3.containerhub.tripleten-services.com?lng=pt")
time.sleep(2)

driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")
time.sleep(1)
driver.find_element(By.ID, "to").send_keys("1300 1st St")
time.sleep(1)
driver.quit()
