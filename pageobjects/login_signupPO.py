from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from .base_page import BasePage
from locators.login_signup_page import LoginSignupPageLocator


class LoginSignupPO(BasePage):
    def __init__(self, driver: webdriver, waittime=3):
        super().__init__(driver, waittime)
        self.locators = LoginSignupPageLocator

    def get_error_text(self):
        return self.driver.find_element(*self.locators.ERROR_FIELD).text

    def click_enter_your_mobile_number_field(self):
        self.driver.find_element(*self.locators.ENTER_MOBILE_NUMBER_INPUT_BTN).click()

    def click_send_via_sms(self):
        self.driver.find_element(*self.locators.SEND_VIA_SMS_BTN).click()

    def enter_mobile_number(self, number):
        self.driver.find_element(
            *self.locators.ENTER_MOBILE_NUMBER_INPUT_FIELD
        ).clear().set_text(number)

    def enter_verify_code(self, code):
        self.driver.find_element(
            *self.locators.ENTER_VERIFY_CODE_INPUT_FIELD
        ).set_text(code)

    def click_next_btn(self):
        self.driver.find_element(
            *self.locators.NEXT_BTN
        ).click()
