# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 22:53
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : conftest.py
# @Software: PyCharm

import pytest
from PageObject.Login_page.login_page import Login_page
from PageObject.Buy_page.buy_page import Buy_page
from PageObject.Register_page.register_page import Register_page


@pytest.fixture(scope="function")
def login_page_class_load(function_driver):
    login_page = Login_page(function_driver)
    yield login_page


@pytest.fixture(scope="function")
def buy_page_class_load(function_driver):
    buy_page = Buy_page(function_driver)
    yield buy_page


@pytest.fixture(scope="function")
def register_page_class_load(function_driver):
    register_page = Register_page(function_driver)
    yield register_page


# if __name__ == '__main__':
#     session_remote_driver()
