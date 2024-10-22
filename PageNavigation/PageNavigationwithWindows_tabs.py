from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Chromedriver setup
service = Service('C:\\Drivers\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

#Url visit
driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
#driver.maximize_window()
time.sleep(2)
#driver.switch_to.new_window('window')
driver.switch_to.new_window('tab')
driver.get("https://www.youtube.com/")
handle=driver.window_handles
driver.switch_to.window(handle[0])
time.sleep(2)
driver.maximize_window()
time.sleep(2)
windowSize=driver.get_window_size()
print(windowSize)
driver.set_window_rect(10,20,400,600)
time.sleep(2)
driver.quit()