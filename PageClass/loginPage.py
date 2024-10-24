# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    def navigate(self):
        self.driver.get(self.url)

    def set_username(self, username):
        username_field = self.driver.find_element(By.ID, "txt-username")
        username_field.clear()
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.driver.find_element(By.ID, "txt-password")
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "btn-login").click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
