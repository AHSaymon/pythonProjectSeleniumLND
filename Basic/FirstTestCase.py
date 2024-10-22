from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Chromedriver setup
service = Service('C:\\Drivers\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

#Url visit
driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")

username=driver.find_element(By.ID,'txt-username')
password=driver.find_element(By.ID,'txt-password')
login=driver.find_element(By.ID,'btn-login')

username.send_keys('John Doe')
password.send_keys('ThisIsNotAPassword')
time.sleep(5)

login.click()
time.sleep(5)

driver.maximize_window()
time.sleep(5)
driver.quit()
