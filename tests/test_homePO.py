import time

import pytest

from .base_test_case import BaseTestCase
from pageobjects.homePO import HomePO
from pageobjects.accountPO import AccountPO
from pageobjects.login_signupPO import LoginSignupPO


class Signup(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()

    def Xtest_Signup_TC_002(self):
        home = HomePO(self.driver_instance, waittime=self.wait_time)
        home.click_my_account_btn()
        time.sleep(self.wait_time)

        account = AccountPO(self.driver_instance, waittime=self.wait_time)
        account.click_login_or_signup_btn()
        time.sleep(self.wait_time)

        login_signup = LoginSignupPO(self.driver_instance, waittime=self.wait_time)
        login_signup.click_enter_your_mobile_number_field()
        time.sleep(self.wait_time)
        login_signup.click_send_via_sms()
        time.sleep(self.wait_time)

        error_text = login_signup.get_error_text()
        self.assertIsNotNone(error_text)
        self.assertEqual(error_text, "Mandatory Field.")

    def Xtest_Signup_TC_003(self):
        home = HomePO(self.driver_instance, waittime=self.wait_time)
        home.click_my_account_btn()
        time.sleep(self.wait_time)

        account = AccountPO(self.driver_instance, waittime=self.wait_time)
        account.click_login_or_signup_btn()
        time.sleep(self.wait_time)

        login_signup = LoginSignupPO(self.driver_instance, waittime=self.wait_time)
        login_signup.click_enter_your_mobile_number_field()
        time.sleep(self.wait_time)
        number = '66666666'
        login_signup.enter_mobile_number(number)
        login_signup.click_send_via_sms()
        time.sleep(self.wait_time)

        error_text = login_signup.get_error_text()
        self.assertIsNotNone(error_text)
        self.assertEqual(error_text, "Please enter a valid phone number.")

    def test_Signup_TC_004(self):
        home = HomePO(self.driver_instance, waittime=self.wait_time)
        home.click_my_account_btn()
        time.sleep(self.wait_time)

        account = AccountPO(self.driver_instance, waittime=self.wait_time)
        account.click_login_or_signup_btn()
        time.sleep(self.wait_time)

        login_signup = LoginSignupPO(self.driver_instance, waittime=self.wait_time)
        login_signup.click_enter_your_mobile_number_field()
        time.sleep(self.wait_time)
        number = '6666666666'
        login_signup.enter_mobile_number(number)
        login_signup.click_send_via_sms()
        time.sleep(self.wait_time * 2)

        code = '111111'
        login_signup.enter_verify_code(code)
        time.sleep(self.wait_time)
        # login_signup.click_next_btn()
        time.sleep(self.wait_time)

        error_text = login_signup.get_error_text()
        self.assertIsNotNone(error_text)
        self.assertEqual(error_text, "Invalid verification code.")
