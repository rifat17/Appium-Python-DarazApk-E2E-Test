from appium.webdriver.common.mobileby import MobileBy


class HomePageLocator:
    MY_ACCOUNT_BTN = (MobileBy.XPATH, '//android.widget.TextView[@text=\"Account\"]')
