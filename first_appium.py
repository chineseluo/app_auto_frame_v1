#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 10:56
# @Author  : luozhongwen
# @Email   : luozw@inhand.com.cn
# @File    : first_appium.py
# @Software: PyCharm

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {
    'platformName': "Android",
    'deviceName': "127.0.0.1:62001",
    'platformVersion': "5.1.1",
    'appPackage': "cn.com.smartfleet.app.admin",
    'appActivity': "cn.com.smartfleet.app.admin.MainActivity",
    'unicodeKeyboard': True,
    'resetKeyboard': True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.find_element()
#driver.implicitly_wait(5)
print(driver.current_activity)
#driver.wait_activity(driver.current_activity, 10, 0.5)
locator_text_1 = 'new UiSelector().text("请输入手机号")'
# driver.find_element_by_android_uiautomator(locator_text_1).send_keys("18383398524")
elem = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_android_uiautomator(locator_text_1))
elem.send_keys("18383398524")
locator_text_2 = 'new UiSelector().text("请输入验证码")'
driver.find_element_by_android_uiautomator(locator_text_2).send_keys("你好啊")
list = driver.find_elements_by_class_name("android.widget.EditText")
for item in list:
    print(item)
