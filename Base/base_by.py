#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : app_auto_frame
@Time    : 2020/6/8 14:42
@Auth    : luozhongwen
@Email   : luozw@inhand.com.cn
@File    : base_by.py
@IDE     : PyCharm
------------------------------------
"""
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class Base_by(By):
    IOS_UIAUTOMATION = MobileBy.IOS_UIAUTOMATION
    IOS_PREDICATE = MobileBy.IOS_PREDICATE
    IOS_CLASS_CHAIN = MobileBy.IOS_CLASS_CHAIN
    ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
    ANDROID_VIEWTAG = MobileBy.ANDROID_VIEWTAG
    WINDOWS_UI_AUTOMATION = MobileBy.WINDOWS_UI_AUTOMATION
    ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID
    IMAGE = MobileBy.IMAGE
    CUSTOM = MobileBy.CUSTOM
