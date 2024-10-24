# tests/test_login.py
import unittest
from utils.webdriverSetup import WebDriverSetup
from PageClass.loginPage import LoginPage
from PageClass.homePage import HomePage

class LoginTest(unittest.TestCase):
    def setUp(self):
        setup = WebDriverSetup()
        self.driver = setup.get_driver()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_valid_login(self):
        self.login_page.navigate()
        self.login_page.login("John Doe", "ThisIsNotAPassword")
        self.home_page.click_make_appointment()
        # Assert if appointment button is clicked and page navigates

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
