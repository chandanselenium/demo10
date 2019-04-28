from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("http://localhost/login.do")
sleep(3)
driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("admin")
sleep(3)
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("manager")
sleep(3)
driver.find_element_by_xpath("//a[@id='loginButton']//div[contains(text(),'Login')]").click()

#get the title
page_title=driver.title

print(page_title)

#wait for few seconds
sleep(2)

#compare the title
if("actiTIME - Enter Time-Track" in page_title):
    print("testing pass")
else:
    print("testing fail")

#close the browser
driver.quit()


