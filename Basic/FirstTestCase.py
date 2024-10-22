from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Chromedriver setup
service = Service('C:\\Drivers\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

#Url visit
driver.get("https://www.youtube.com/")

time.sleep(10)