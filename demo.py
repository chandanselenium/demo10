from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/CHANDAN%20V/Desktop/demo.html")
#driver.find_element(By.ID,'a1').click()
#driver.find_element(By.NAME,'a12').click()
#driver.find_element(By.CLASS_NAME,'a123').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'googl').click()
