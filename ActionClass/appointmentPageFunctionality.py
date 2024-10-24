# tests/test_appointment.py
import unittest
from utils.webdriverSetup import WebDriverSetup
from PageClass.loginPage import LoginPage
from PageClass.homePage import HomePage
from PageClass.appointmentPage import AppointmentPage

class AppointmentTest(unittest.TestCase):
    def setUp(self):
        setup = WebDriverSetup()
        self.driver = setup.get_driver()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.appointment_page = AppointmentPage(self.driver)

    def test_book_appointment(self):
        # Login and navigate to appointment page
        self.login_page.navigate()
        self.login_page.login("John Doe", "ThisIsNotAPassword")
        self.home_page.click_make_appointment()

        # Book an appointment
        self.appointment_page.select_facility("Tokyo CURA Healthcare Center")
        self.appointment_page.check_hospital_readmission()
        self.appointment_page.select_healthcare_program("Medicare")
        self.appointment_page.set_visit_date("10/22/2024")
        self.appointment_page.set_comment("Regular checkup")
        self.appointment_page.book_appointment()

        # Add assertions based on the booking success page or message

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
