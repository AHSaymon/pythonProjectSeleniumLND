from time import thread_time

from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from Basic.FirstTestCase import login

#Chromedriver setup
service = Service('C:\\Drivers\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

#Url visit
driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")


loginBtn=driver.find_element(By.ID,'btn-login')

#action Object
actions=ActionChains(driver)

actions.context_click(on_element=loginBtn).perform()
time.sleep(2)

actions.click_and_hold(on_element=loginBtn).perform()

time.sleep(2)

actions.move_by_offset(40,10).perform()

actions.release().perform()


