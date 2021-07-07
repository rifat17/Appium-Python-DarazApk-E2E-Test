from appium import webdriver
from unittest import TestCase
import time


class BaseTestCase(TestCase):

    def setUp(self) -> None:
        desired_caps = dict(
            platformName='Android',
            platformVersion='11',
            automationName='uiautomator2',
            deviceName='emulator-5554',
            # appPackage='com.daraz.android',
            # appActivity='com.lazada.activities.EnterActivity',
            app='/home/hasib/PycharmProjects/AppiumDarazApk/resourses/daraz.apk'
        )
        self.wait_time = 3
        self.driver_instance = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        self.load_home()

    def load_home(self):
        self.driver_instance.find_element_by_xpath('//android.widget.TextView[@text="Bangladesh"]').click()
        time.sleep(self.wait_time)
        self.driver_instance.find_element_by_id('android:id/button1').click()
        time.sleep(self.wait_time)
        self.driver_instance.find_element_by_id('com.daraz.android:id/intro_skip_btn').click()
        time.sleep(self.wait_time)

    def tearDown(self) -> None:
        self.driver_instance.quit()
