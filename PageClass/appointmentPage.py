# pages/appointment_page.py
from selenium.webdriver.common.by import By

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver

    def select_facility(self, facility):
        facility_dropdown = self.driver.find_element(By.ID, "combo_facility")
        facility_dropdown.send_keys(facility)

    def check_hospital_readmission(self):
        self.driver.find_element(By.ID, "chk_hospotal_readmission").click()

    def select_healthcare_program(self, program):
        program_radio = self.driver.find_element(By.XPATH, f"//input[@name='programs'][@value='{program}']")
        program_radio.click()

    def set_visit_date(self, date):
        self.driver.find_element(By.ID, "txt_visit_date").send_keys(date)

    def set_comment(self, comment):
        self.driver.find_element(By.ID, "txt_comment").send_keys(comment)

    def book_appointment(self):
        self.driver.find_element(By.ID, "btn-book-appointment").click()
