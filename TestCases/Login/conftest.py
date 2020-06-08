# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 22:53
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : conftest.py
# @Software: PyCharm
import pytest
from ActivityObject.Login_activity.login_activity import Login_activity


@pytest.fixture(scope="function")
def login_page_class_load(function_driver):
    login_activity = Login_activity(function_driver)
    yield login_activity


