from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from .base_page import BasePage
from locators.account_page import AccountPageLocator


class AccountPO(BasePage):
    def __init__(self, driver: webdriver, waittime=3):
        super().__init__(driver, waittime)
        self.locators = AccountPageLocator

    def click_login_or_signup_btn(self):
        self.driver.find_element(*self.locators.LOGIN_SIGNUP_TEXT).click()

