# utils/webdriver_setup.py
from selenium import webdriver

class WebDriverSetup:
    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()
