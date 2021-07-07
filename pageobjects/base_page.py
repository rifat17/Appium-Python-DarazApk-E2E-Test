import time

from appium import webdriver
from enum import Enum


class BasePage:
    def __init__(self, driver: webdriver.Remote, waittime=10):
        self.driver = driver
        self.wait_time = waittime

    def scroll_to(self, direction: str):
        self.driver.execute_script("mobile: scroll", {'direction': direction})
