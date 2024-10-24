from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Chromedriver setup
service = Service('C:\\Drivers\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

#Url visit
driver.get("https://www.google.com/")


#search=driver.find_element(By.NAME,'q')
#driver.implicitly_wait(5)
#search.click()
driver.implicitly_wait(5)
#search.send_keys('Abc')
# Explicit wait
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

# Example: Wait for element to be clickable
element = wait.until(EC.element_to_be_clickable((By.ID, 'q')))
element.click()
