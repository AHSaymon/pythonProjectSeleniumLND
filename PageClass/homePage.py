# pages/home_page.py
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_make_appointment(self):
        self.driver.find_element(By.ID, "btn-make-appointment").click()
