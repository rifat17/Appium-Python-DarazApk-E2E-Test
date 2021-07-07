from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from .base_page import BasePage
from locators.home_page import HomePageLocator


class HomePO(BasePage):
    def __init__(self, driver: webdriver, waittime=3):
        super().__init__(driver, waittime)
        self.locators = HomePageLocator

        # self.my_account = WebDriverWait(self.driver, waittime).until(
        #     EC.visibility_of_element_located((
        #         MobileBy.XPATH, '//android.widget.TextView[@text=\"Account\"]'))
        # )
        #
        # self.login_or_signup = WebDriverWait(self.driver, waittime).until(
        #     EC.visibility_of_element_located((
        #         MobileBy.ID, 'com.daraz.android:id/txt_login_signup'))
        # )
        #
        # self.enter_your_mobile_number_field = WebDriverWait(self.driver, waittime).until(
        #     EC.visibility_of_element_located((
        #         MobileBy.ID, 'com.daraz.android:id/tv_signup'
        #     ))
        # )
        #
        # self.send_via_sms = WebDriverWait(self.driver, waittime).until(
        #     EC.visibility_of_element_located((
        #         MobileBy.ID, 'com.daraz.android:id/btn_send_sms_code'
        #     ))
        # )

    def click_my_account_btn(self):
        # self.my_account.click()
        self.driver.find_element(*self.locators.MY_ACCOUNT_BTN).click()
