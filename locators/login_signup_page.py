from appium.webdriver.common.mobileby import MobileBy


class LoginSignupPageLocator:
    ENTER_MOBILE_NUMBER_INPUT_BTN = (MobileBy.ID, 'com.daraz.android:id/tv_signup')
    SEND_VIA_SMS_BTN = (MobileBy.ID, 'com.daraz.android:id/btn_send_sms_code')
    ERROR_FIELD = (MobileBy.ID, 'com.daraz.android:id/tv_label')
    ENTER_MOBILE_NUMBER_INPUT_FIELD = (MobileBy.ID, 'com.daraz.android:id/et_input_content')
    ENTER_VERIFY_CODE_INPUT_FIELD = (MobileBy.ID, 'com.daraz.android:id/verify_code_view')
    NEXT_BTN = (MobileBy.ID, 'com.daraz.android:id/btn_next')
